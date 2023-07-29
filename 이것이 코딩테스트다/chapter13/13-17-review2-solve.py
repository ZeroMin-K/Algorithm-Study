"""
n * n 크기 시험관. 1 * 1 크기로 나누어지며 특정 위치 바이러스 존재
모든 바이러스는 1번부터 k번까지 바이러스 종류 중 하나에 속함
시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식
매초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
특정칸에 이미 바이러스 존재지 다른 바이러스는 불가

s초가 지난 후 (x, y)에 존재하는 바이러스 종류 출력.
    x, y는 행과열. 가장 왼쪽위는 (1, 1)
s초가 지난 후 해당 위치 바이러스 존재하지 않는다면 0출력

각 바이러스를 bfs를 통해 증식시키는데 
이때 시간 초가 더 빠른게 먼저 자리를 차지하고 그다음 바이러스 작은것이 차지 
"""
# 빠른 입력
import sys
input = sys.stdin.readline

# n, k 입력
n, k = map(int, input().split())
# 시험관에 대한 2차원 리스트 graph : 빈리스트로 초기화
graph = [] 
# 각 바이러스 시작 위치에 대한 리스트 viruses : 빈리스트로 초기화 
viruses = [] 
# 시험관 각 위치에 대해 시간을 기록하는 times 2차원 리스트 값은 10001로 n * n 크기 
times = [[10001] * n for _ in range(n)]
# 인덱스 i: 0부터 n - 1까지 반복하면서
for i in range(n): 
    # 한 줄을 입력받아 split으로 나눈후 int로 map한 후 list로 변환한 data 리스트
    data = list(map(int, input().split()))
    # graph에 data 삽입
    graph.append(data)
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(n):
        # data[j] 가 0이 아니면
        if data[j] != 0:
            # viruses에 (i, j) 삽입
            viruses.append((i, j))
            # times[i][j] 는 0으로 값 변경 
            times[i][j] = 0

# s, x, y 입력 
s, x, y = map(int, input().split()) 

# deque import 
from collections import deque 
# x, y 상, 하, 좌우로 움직일때에 대한 moves 리스트 생성 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 함수 선언 : 인자 start_x, start_y
def bfs(start_x, start_y):
    # 큐 q deque로 생성 
    q = deque()
    # 큐에 (start_x, start_y) 삽입
    q.append((start_x, start_y))
    # 현재 바이러스 종류 type 은 graph[start_x][start_y]
    type = graph[start_x][start_y]
    # 큐가 빌때까지 반복 
    while q:
        # 큐에서 원소 꺼냄. 현재 바이러스 위치 x, y
        x, y = q.popleft()
        # 다음 위치에서 증식시간 next_time은 time[now[0]][now[1]] + 1
        next_time = times[x][y] + 1
        
        # next_time이 s보다 크면 
        if next_time > s:
            # break
            break
        
        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves: 
            # 다음 x좌표 nx는 now[0] + move[0]을 더함
            nx = x + move[0]
            # 다음 y좌표 ny는 now[1] + move[1]을 더함 
            ny = y + move[1]
            
            # nx, ny가 0보다 같거나 크거나 n보다 작으면
            if 0 <= nx < n and 0 <= ny < n:
                # time[nx][ny]보다 next_time이 작거나
                # times[nx][ny]와 next_time이 같고 graph[nx][ny]보다 type이 작으면
                if times[nx][ny] > next_time or \
                    (times[nx][ny] == next_time and graph[nx][ny] > type):
                    # time[nx][ny]는 next_time으로 변경
                    times[nx][ny] = next_time
                    # graph[nx][ny]는 type 
                    graph[nx][ny] = type
                    # (nx, ny)를 큐에 삽입
                    q.append((nx, ny))

# viruses를 하나씩 탐색하면서 : 원소 virus
for virus in viruses: 
    # virus[0], virus[1]부터 BFS 진행
    bfs(virus[0], virus[1])

# s초후 (x, y)에 존재하는 바이러스 출력 (없으면 0) 
print(graph[x - 1][y - 1])