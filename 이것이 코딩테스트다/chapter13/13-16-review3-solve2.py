"""
n * m 크기의 연구소 - 1 * 1 크기 정사각형으로 나누어짐 
연구소는 빈칸, 벽으로 이루어지고 벽 칸하나 가득 차지
    0: 빈칸, 1: 벽, 2: 바이러스
일부 칸은 바이러스가 존재. 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나감 
새로 세울 수 있는 벽의 개수 3개 무조건 3개 세우기 

벽 3개 세운뒤 바이러스가 퍼질 수 없는 곳을 안전 영역이라함
안전영역 크기의 최댓값 계산하기 
"""

# 세로 크기 n, 가로크기 m 입력 
n, m = map(int, input().split())
# 연구소 리스트 labs 빈 리스트로 생성 
labs = [] 
# 빈칸 위치를 저장하는 리스트 blanks 
blanks = [] 
# 인덱스 i: 0부터 n - 1까지 반복하면서
for i in range(n): 
    # 한 줄 입력해 공백구분으로 나누고 int로 map하여 리스트로 변경한 data
    data = list(map(int, input().split()))
    # labs에 data 삽입 
    labs.append(data)
    # 인덱스 j: 0부터 m - 1까지 반복하면서 
    for j in range(m):
        # data[j]가 0이면
        if data[j] == 0:
            # blanks에 (i, j) 삽입 
            blanks.append((i, j))

# 안전영역 크기를 세는 함수 count_safe 선언 : 매개변수 labs
def count_safe(labs):
    # 안전영역 크기 safe 0으로 초기화
    safe = 0
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n):
        # 인덱스 j: 0부터 m - 1까지 반복하면서
        for j in range(m):
            # labs[i][j]가 0이면
            if labs[i][j] == 0:
                # safe 1증가
                safe += 1
    # safe 리턴 
    return safe

# deque import 
from collections import deque 
# 상, 하, 좌, 우 x,y좌표 위치 담는 moves 리스트
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# bfs 선언 시작좌표 start, 연구소 좌표리스트 labs
def bfs(start, labs):
    # start을 인자로 큐 q를 deque로 생성
    q = deque()
    q.append(start)
    
    # q가 빌때까지 반복하면서
    while q: 
        # 현재 x좌표, y좌표는 q에서 popleft한것
        x, y = q.popleft() 
        
        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves: 
            # 다음 x좌표 nx는 x + move[0]
            nx = x + move[0] 
            # 다음 y좌표 ny는 y + move[1]
            ny = y + move[1] 
            
            # nx와 ny가 0보다 작거나 nx가 n보다 같거나 크거나 ny가 m보다 같거나 크면
            if nx < 0 or ny < 0 or nx >= n or ny >= m: 
                # continue
                continue 
                
            # labs[nx][ny]가 0이면
            if labs[nx][ny] == 0:
                # labs[nx][ny] 는 2로 변경
                labs[nx][ny] = 2
                # 큐에 (nx, ny) 삽입 
                q.append((nx, ny))

# 최대 안전 영역 크기 max_safe 0으로 초기화 
max_safe = 0 
# copy import 
import copy 

def spread_virus(labs):
    for i in range(n):
        for j in range(m):
            if labs[i][j] == 2:
                bfs((i, j), labs)

def dfs(walls, labs):
    global max_safe
    if walls == 3:
        new_labs = copy.deepcopy(labs)
        spread_virus(new_labs)
        max_safe = max(count_safe(new_labs), max_safe)
        return 
    elif walls > 3:
        return 
    
    for i in range(n):
        for j in range(m):
            if labs[i][j] == 0:
                labs[i][j] = 1
                dfs(walls + 1, labs)
                labs[i][j] = 0

dfs(0, labs) 

# 안전 영역의 최대 크기 max_safe 출력 
print(max_safe)