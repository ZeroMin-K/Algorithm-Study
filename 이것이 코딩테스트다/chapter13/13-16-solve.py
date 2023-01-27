"""
바이러스 확산 막기위해 벽 설치하기
N * M 크기 직사각형 연구소 - 1 * 1크기의 정사각형
연구소는 빈칸, 벽 - 벽은 칸 하나 차지
바이러스는 상하좌우로 인접한 빈칸 모두 퍼져나감
세울 수 있는 벽의 개수 3개 무조건 3개만 
벽 3개 세우고 바이러스가 퍼질 수 없는 곳을 안전영역.
안전 영역 크기의 최댓값 구하는 프로그램 작성 

벽 3개를 세우고 
바이러스 위치에 따라 bfs 진행
전부 읽으면서 안전영역 수 세기 

"""

# 지도 세로 크기, 가로크기 n, m 입력 
n, m = map(int, input().split())

# 연구소 2차원 리스트 생성
lab = [[0] * m for _ in range(n)]
# 바이러스 위치 리스트 
virus_loc = []
# 벽 세울 수 있는 공간 리스트 
walls = []

# n개 반복하면서
for i in range(n):
    # 지도 모양 입력 - 0: 빈칸, 1:벽, 2:바이러스 
    data = list(map(int, input().split()))
    # 연구소 리스트에 추가
    for j in range(m):
        lab[i][j] = data[j]

        # 바이러스 위치를 따로 저장 
        if data[j] == 2:
            virus_loc.append((i, j))

        # 벽을 세울 수 있는 위치 저장
        elif data[j] == 0:
            walls.append((i, j))

from collections import deque

# 상, 하, 좌, 우로 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 이용하여 바이러스 확산 
def spread_virus(start, graph):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        # 현재 위치에서 다음 위치로 바이러스 확산
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 다음 위치의 인덱스가 맞으면 
            if 0 <= next_x < n and 0 <= next_y < m:
                # 해당 위치 바이러스로 감염 
                if graph[next_x][next_y] == 0:
                    graph[next_x][next_y] = 2

                    # 큐에다 해당 위치 삽입
                    q.append((next_x, next_y))

# 안전 영역의 크기 최댓값 저장하는 변수 
max_safe = 0 

from itertools import combinations
import copy

# 벽을 세울 수 있는 3개 위치에 대한 combination을 반복하면서
for wall_candis in list(combinations(walls, 3)):
    # 연구소 리스트 복사해서 새로운 리스트 생성
    new_lab = copy.deepcopy(lab)
    # 현재 combination에 대한 벽 세우기
    for wall_candi in wall_candis:
        new_lab[wall_candi[0]][wall_candi[1]] = 1

    # 바이러스 위치 리스트를 하나씩 읽으면서 
    for virus in virus_loc:
        # 현재 바이러스에서부터 BFS 진행
        spread_virus((virus[0], virus[1]), new_lab)
        
    # 현재 안전 영역 수
    now_safe = 0
    # 안전 영역의 수 세기
    for i in range(n):
        for j in range(m):
            if new_lab[i][j] == 0:
                now_safe += 1

    # 이전 안전 영역의 크기와 현재 안전영역의 크기 비교해서 더 큰수 저장
    max_safe = max(max_safe, now_safe)

#  안전 영역 크기 출력 
print(max_safe)