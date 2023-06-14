"""
사과를 먹으면 뱀 길이 늘어남. 벽, 자기자신의 몸과 부딪히면 게임 종료
N * N 정사각 보드 위 진행. 상, 하, 좌, 우 끝 벽에 있음
시작시 뱀은 맨위 맨좌측 위치. 뱀의 길이 1. 처음에 오른쪽으로 향함. 매초마당 이동
이동 규칙
- 몸길이를 늘려 머리를 다음칸에 위치
- 벽이나 자기자신의 몸과 부딪히면 게임 종료
- 이동한 칸에 사과가 있다면 그 칸 사과가 없어지고 꼬리 움직이지 않음
- 만약 이동한 칸에 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비워준다, 몸길이는 변하지 않음
사과의 위치, 뱀 이동경로 입력, 몇초에 끝나는지 계산 

데큐를 이용하여 머리를 위치를 계속해서 가장 첫번째 더해주고 가장 끝 부분은 pop해주며 꼬리이동 (몸길이 변화X)
사과있을때만 pop하지 않음 
머리가 이동할때 벽에 부딪히거나 자기자신의 몸에 부딪히는지 확인 


"""
from collections import deque

# 보드의 크기 n 입력
n = int(input())
# 사과 개수 k 입력
k = int(input())

# 보드 리스트 생성 n * n 2차원 리스트 값은 0으로 초기화 
board = [[0] * n for _ in range(n)]
# k번 반복하면서 
for _ in range(k):
    # 사과의 행, 열 위치 입력 (1행 1열 시작이라 둘다 -1로 입력)
    a, b = map(int, input().split())
    # 보드 리스트에 1로 값을 저장 
    board[a - 1][b - 1] = 1

# 뱀의 방향 변환 횟수 L 입력 
L = int(input())
# 뱀 방향 전환 리스트를 비어있는 deque로 초기화 
turns = deque() 
# L번반복하면서
for _ in range(L):
    # 뱀의 방향 정보 입력. 정수 X. 문자 C 입력. x초가 끝난뒤 왼쪽 L, 오른쪽 D로 90도 회전
    x, c = input().split()
    turns.append((int(x), c))

# 현재 게임 종료 시간 0으로 초기화 
time = 0
# 현재 뱀의 머리 방향. 오른쪽으로 이동하니 1로 초기화 (상 0, 우 1, 하 2, 좌 3)  
head = 1 
# 뱀의 머리, 몸, 꼬리 위치를 담는 deque 리스트 생성 - 현재 위치는 0, 0
snake = deque([(0, 0)])


# 인덱스 i: 1초부터 이동하기 시작해서 최대 10000까지 진행하면서 
for i in range(1, 10000):
    # 현재 뱀의 머리 방향에 맞게 이동했을 때 다음의 머리 방향 (상 0, 우 1, 하 2, 좌 3)
    forwards = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    next_head_x = snake[0][0] + forwards[head][0] 
    next_head_y = snake[0][1] + forwards[head][1]

    # 뱀의 머리가 벽에 붙이거나 자기자신의 몸에 부딪히면 
    if (next_head_x < 0 or next_head_x >= n or next_head_y < 0 or next_head_y >= n) or \
        (next_head_x, next_head_y) in snake:
        # 현재 초를 저장
        time = i
        # 반복 종료 
        break
    # 뱀의 머리위치가 사과이면
    elif board[next_head_x][next_head_y] == 1:
        # 사과 위치를 없앰
        board[next_head_x][next_head_y] = 0
        # 뱀의 꼬리 위치 변하지 않음
    # 나머지 경우 
    else: 
        # 뱀의 꼬리 위치 제거 
        snake.pop() 
    
    # 뱀 리스트에 현재 뱀머리 위치를 앞에 붙임 
    snake.appendleft((next_head_x, next_head_y))

    # 방향 전환 리스트에서 초에 맞게 머리 방향 회전 
    if len(turns) > 0 and i == turns[0][0]:
        # 머리방향 (상 0, 우 1, 하 2, 좌 3) 왼쪽 회전이면 -1, 오른쪽 회전이면 + 1
        head = head + 1 if turns[0][1] == 'D' else head - 1
        if head > 3:
            head = 0
        elif head < 0:
            head = 3 
    
        turns.popleft() 

# 게임 종료 시간 출력 
print(time) 