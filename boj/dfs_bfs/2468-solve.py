"""
비가 내렸을 때 물에 잠기지 않는 안전한 영역최대로 몇개인지
비의 양에 따라 일정한 높이 이하의 모든 지점은 물에잠김
행, 열 크기n인 2차원 배열. 해당 지점의 높이를 표시
안전한 영역: 위,아래, 오른쪽, 왼쪽 인접. 크기가 최대 

어떤 지역 높이 정보가 주어지면 안전영역 최대 개수 계산 
"""

# 행, 열의 개수 n 입력 (2 <= n <= 100) 
n = int(input())
# 영역 리스트 생성
graph = []
# n번 반복하며
for _ in range(n):
    # 각 행에 대한 높이 정보가 공백 구분으로 입력  (1이상 100이하)
    graph.append(list(map(int, input().split())))

# 상, 하, 좌, 우 좌표 생성 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 큐 import 
from collections import deque
# bfs 선언
def bfs(visited, water, now):
    # 큐 생성
    q = deque()
    # 현재 위치 넣기
    q.append(now)
    # 현재 위치 방문 처리 
    visited[now[0]][now[1]] = 1
    
    # 큐가 빌때까지 반복
    while q: 
        # 현재 위치
        x, y = q.popleft()

        # 상, 하, 좌, 우 이동하면서
        for move in moves: 
            next_x = x + move[0]
            next_y = y + move[1]

            # 다음좌표가 좌표 범위안에 있고 
            if 0 <= next_x < n and 0 <= next_y < n:
                # 방문 하지 않았으며 물에 잠기지 않으면
                if visited[next_x][next_y] == 0 and graph[next_x][next_y] > water:
                    # 방문처리하고 
                    visited[next_x][next_y] = 1
                    # 큐에 삽입 
                    q.append((next_x, next_y))

# 안전 영역 최대 개수 0
max_safe = 0
# 물의 높이 정보 water : 1부터 n까지 반복하며 
for water in range(101):
    # 현재 물의 높이에서 안전 영역 개수 0
    safe = 0
    # 방문했는지 여부 리스트 
    visited = [[0] * n for _ in range(n)]
    # 행 인덱스 i  : 0부터 n - 1까지 반복하며   
    for i in range(n):
        # 열 인덱스 j : 0부터 n - 1까지 반복하며
        for j in range(n):
            # 현재 위치가 물의 높이 정보보다 크고, 방문하지 않았으면 
            if graph[i][j] > water and visited[i][j] == 0:
                # 현재 위치에서 bfs 진행 
                bfs(visited, water, (i, j))
                # 안전 영역 개수 1 증가
                safe += 1
    # 모든 영역을 돌았을 때 현재 안전영역개수와 최대개수 비교해서 최대 값 구하기
    max_safe = max(max_safe, safe)

# 최대값 리턴 
print(max_safe)