"""
n * n 정사각 보드위 몇몇 칸에 사과가 있음
보드의 상하좌우 끝에 벽이 있음
게임이 시작할때 뱀은 맨 좌측에 위치, 뱀의 길이는 1. 오른쪽을 향함
뱀은 매초마다 이동. 
- 뱀은 몸길이를 늘려 머리를 다음칸에 위치
- 벽이나 자기자신의 몸과 부딪히면 게임이 끝남
- 이동한 칸에 사과가 있으면 사과가 없어지고 꼬리는 움직이지 않음
- 이동한 칸에 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비워줌
    - 몸의 길이 변하지 않음 
사과의 위치, 뱀의 이동경로 주어지면 게임이 몇초에 끝나는지 계산 
"""
# deque import 
from collections import deque 

# 빠른 입력
import sys
input = sys.stdin.readline 

# 보드의 크기 n 입력 
n = int(input()) 

# 보드 정보 board는 원소는 [0]으로 n * n 크기로 초기화 
board = [[0] * n for _ in range(n)]

# 사과의 개수 k 입력 
k = int(input()) 
# k번 반복하면서 
for _ in range(k): 
    # 사과의 위치 행 a, 열 b 입력 
    a, b = map(int, input().split())
    # board[a][b]는 1
    board[a - 1][b - 1] = 1
    
# 뱀의 방향 변환횟수 L 입력
l = int(input()) 
# 뱀의 방향 변환 정보를 저장하는 리스트 rotates deque로 생성 
rotates = deque() 
# l번 반복하면서 
for _ in range(l): 
    # x, c 입력 (x초가 끝난뒤 회전. L: 왼쪽 회전, D : 오른쪽 회전 )
    x, c = input().split()
    # (x, c)를 rotates에 삽입 
    rotates.append((int(x), c)) 
    
# 현재 향하는 방향 dir 0
dir = 0 
# 움직임 우, 하, 좌, 상 
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 머리 방향 회전하는 함수 rotate_head: 매개변수 방향 정보 next
def rotate_head(next): 
    global dir 
    
    # next가 'L'이면 
    if next == 'L':
        # dir - 1이 0보다 작으면 dir은 moves의 길이 - 1 아니면 dir - 1
        dir = len(moves) - 1 if dir - 1 < 0 else dir - 1 
    # 나머지 경우 
    else: 
        # dir은 dir + 1을 moves의 길이로 나눈 나머지 값 
        dir = (dir + 1) % len(moves) 
        
# 뱀의 현재 좌표 x, y 는 0, 0으로 초기화 
x, y = 0, 0 
# 뱀의 몸통 좌표 리스트 snakes deque로 생성
snakes = deque() 
# snakes에 (x, y) 삽입 
snakes.append((x, y)) 

# 현재 시간 time 0초 
time = 0 
# 무한 반복 
while True: 
    # time 1 증가 
    time += 1
    # 다음 좌표 x, y는 snakes[0][0] + moves[dir][0], sankes[0][1] + moves[dir][1]
    x, y = snakes[0][0] + moves[dir][0], snakes[0][1] + moves[dir][1] 
    
    # x가 0보다 작거나 n보다 같거나 크거나 y가 0보다 작거나 n보다 같거나 크거나
    # snakes 안에 x, y가 있으면 
    if x < 0 or x >= n or y < 0 or y >= n or \
        (x, y) in snakes: 
        # 종료 
        break 
    
    # (x, y)를 snakes왼쪽에 삽입 
    snakes.appendleft((x, y))
    
    # board[x][y]가 사과이면
    if board[x][y] == 1: 
        # board[x][y]는 0으로 변경
        board[x][y] = 0 
    # 사과가 아니면
    else: 
        # snakes pop
        snakes.pop() 
    
    # rotates가 비어있지 않고 rotates[0][0]과 time이 같으면
    if rotates and rotates[0][0] == time:
        # 머리방향 회전
        rotate_head(rotates.popleft()[1])
        
# time 출력 
print(time)