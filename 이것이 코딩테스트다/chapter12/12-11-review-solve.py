"""
뱀이 나와서 기어다님. 사과를 먹으면 뱀의 길이가 늘어남
벽또는 자기자신의 몸과 부딪히면 게임오버
n * n 정사각 보드위, 몇몇 칸에는 사과. 상, 하, 좌, 우 끝에 벽
게임 시작시 뱀은 맨위 맨좌측에 위치. 뱀의 길이1. 오른쪽으로 향함
뱀은 매초마다 이동
- 뱀은 몸길이를 늘려 머리를 다음칸에 위치
- 만약 벽이나 자기자신의 몸과 부딪히면 게임오버
- 만약 이동한 칸에 사과가 있다면 그 칸에 있떤 사과가 없어지고 꼬리는 움직이지 않음
- 만약 이동한 칸에 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸 비워줌 (몸길이 변하지않음)
- 사과는 1, 1에는 없음 
이 게임이 몇초에 끝나는지 계산 
"""
import sys 
input = sys.stdin.readline

# deque import 
from collections import deque 
# 보드의 크기 n입력
n = int(input())
# 사과의 개수 k 
k = int(input()) 
# 보드 2차원 리스트 board 생성 [0]을 원소로 (n + 1) * (n + 1)크기 
board = [[0] * (n + 1) for _ in range(n + 1)]
# k번 반복하면서
for _ in range(k):
    # 사과 행, 열 위치 a, b 입력 
    a, b = map(int, input().split())
    # board[a][b]는 1로 변경 
    board[a][b] = 1
# 뱀의 방향 변환횟수 L 입력
l = int(input())
# 방향변환 시간, 방향을 저장하는 turns 리스트 빈리스트로 deque 생성
turns = deque([])
# L번 반복하면서
for _ in range(l):
    # x, c 입력 x초부터 끝난뒤 c가 L이면 왼쪽, c가 D이면 오른쪽 90도 방향 회전 
    x, c = input().split()
    # turns에 (x, c) 입력 
    turns.append((int(x), c))

# 상, 우, 하, 좌로 이동하는 움직임 리스트 moves
moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 뱀의 머리, 몸 좌표를 저장하는 snakes 리스트 (1, 1)을 원소로하는 리스트로 deque 생성
snakes = deque() 
snakes.append((1, 1))
# 현재 머리 방향 head 1로 초기화 
head = 1

# 현재 시간 time 0으로 초기화 
time = 0 
# 무한반복
while True: 
    if not snakes:
        break 

    # 뱀의 머리 다음 x좌표 next_head_x는 snakes[0][0]에 moves[head][0]을 더함
    next_head_x = snakes[0][0] + moves[head][0] 
    # 뱀의 머리 다음 y좌표 next_head_y는 sankes[0][1]에 moves[head][1]을 더함 
    next_head_y = snakes[0][1] + moves[head][1] 
    # time 1 증가 
    time += 1

    # time이 turns[0][0]과 같으면
    if turns and time == turns[0][0]:
        # turns popleft하여 turn 생성
        turn = turns.popleft() 
        # turn[1]이 L 이면
        if turn[1] == 'L':
            # 왼쪽 회전
            # head 1 감소 
            # head가 0보다 작으면 head는 3
            head = len(moves) - 1 if head - 1 < 0 else head - 1
        # turn[1]이 D이면
        elif turn[1] == 'D':
            # 오른쪽 회전 
            # head 1증가
            # head가 3보다 크면 head는 0 
            head = 0 if head + 1 >= len(moves) else head + 1

    # snakes안에 (next_head_x, next_head_y)가 있으면 \
    # next_head_x가 1보다 작거나 n보다 크거나 next_head_y가 1보다 작거나 n보다 크면
    if (next_head_x, next_head_y) in snakes or \
        next_head_x < 1 or next_head_x > n or next_head_y < 1 or next_head_y > n: 
        # 반복 종료 
        break

    # sankes에 (next_head_x, next_head_y)을 왼쪽에 삽입 
    snakes.appendleft((next_head_x, next_head_y))
    # board[next_head_x][next_head_y]가 1이면 (사과이면) 
    if board[next_head_x][next_head_y] == 1:
        # 사과 없앰 
        board[next_head_x][next_head_y] = 0
    else:
        # snakes에서 pop
        snakes.pop() 

# 게임이 몇초에 끝나는지 계산
print(time) 