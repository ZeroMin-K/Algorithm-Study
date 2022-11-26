"""
N * M 크기의 얼음틀 - 구멍이 뚫려있는 곳 0, 칸막이가 존재하는 부분 1
구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결 간주 
생성되는 아이스크림의 개수 구하는 프로그램 작성 

얼음틀 좌표를 하나씩 방문하면서
    BFS를 진행 
    연결된 곳은 하나씩 방문처리 - 나중에 이미 방문하지 않게 
    bfs를 진행다 하면 아이스크림 개수 증가 
"""

# 큐 생성을 위한 deque 라이브러리 import 
from collections import deque

# 얼음틀의 세로길이 n, 가로길이 m 입력 
n, m = map(int, input().split())

# 얼음틀 리스트 생성 
tray = []
# n번 반복하며
for _ in range(n):
    # 얼음틀의 형태 입력하며 얼음를 리스트에 append
    tray.append(list(map(int, input())))
        
# x좌표 이동 리스트  - 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
# y좌표 이동 리스트
dy = [0, 0, -1, 1]

# BFS 함수 선언 - 현재 좌표
def bfs(x, y):
    # 현재 좌표 큐에 삽입
    q = deque()
    q.append((x, y))
    # 현재 좌표 방문 표시 
    tray[x][y] = 1
    
    # 큐가 빌때까지 반복하며
    while q:
        # 큐에서 원소 하나 deque
        now_x, now_y = q.popleft()
        
        # 이동 리스트 하나씩 반복 하며 
        for i in range(4):
            # 다음 좌표계산
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            
            # 다음 좌표가 인덱스가 올바르고 
            if 0 <= next_x and next_x < n and 0 <= next_y and next_y < m:
                # 구멍이 뚫려있는 곳이면
                if tray[next_x][next_y] == 0:
                    # 다음 좌표 방문 표시
                    tray[next_x][next_y] = 1
                    # 큐에 삽입  
                    q.append((next_x, next_y))

# 아이스크림 개수 = 0
count = 0 
# 얼음틀 좌표 행 반복하면서
for i in range(n):
    # 얼음틀 좌표 열 반복하면서 
    for j in range(m):
        # 현재 좌표가 뚫려 있는 부분이면
        if tray[i][j] == 0:
            # BFS 진행
            bfs(i, j)
            # 아이스크림 개수 증가
            count += 1
            
# 아이스크림 개수 출력
print(count)