"""
1번부터 N번까지 도시, M개의 단방향 도로, 모든 도로거리 1
특정한 도시 x로부터 출발하여 도달할 수 있는 모든 도시 중 최단거리 K인 모든 도시 번호 출력
출발도시x에서 x로 가는 최단거리는 0
모든 도로거리가 1이기 때문에 BFS를 이용하여 정확하게 거리가 k인 도시 찾기 
"""

# 빠른 입력을 위한 input 변경
import sys
input = sys.stdin.readline

# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발 도시 번호 x
n, m, k , x = map(int, input().split())

# 도시 경로 리스트  (n + 1) 길이 
graph = [[] for _ in range(n + 1)]
# 도시 거리 리스트 (n + 1)길이 원소는 0 
visited = [0] * (n + 1) 

# m번 반복하면서 
for _ in range(m):
    # a, b 공백을 기준으로 구분되어 입력 - a번 도시에서 b번 도시로 이동하는 단방향 도로 존재 
    a, b = map(int, input().split())
    # 도시경로 리스트[a]번째에 b append
    graph[a].append(b)

# deque import 
from collections import deque 
# bfs 선언
def bfs(start):
    # deque 선언
    q = deque()
    # deque에 현재 출발 위치 append
    q.append((start, 0))
    # 출발위치는 -1 처리(나중에 방문하지 않게) 
    visited[start] = -1

    # 큐가 빌때까지 반복하면서
    while q: 
        # 큐에서 현재 도시 반환, 거리 반환 
        city, dist = q.popleft()
        # 현재 도시로부터 연결된 거리 반복하면서
        for next_city in graph[city]:
            # 방문하지 않앗으면(방문리스트가 0)이면 
            if visited[next_city] == 0:
                # 현재 도시를 거리에서 + 1해서 더함
                visited[next_city] = dist + 1
                # 큐에 삽입 
                q.append((next_city, visited[next_city]))

# bfs 실행 ( 출발도시 x)
bfs(x)

# 거리가 k인 도시가 있는지 확인 여부 = False
k_exist = False 

# 도시 거리 리스트 원소 하나씩 확인하면서 
for i in range(1, n + 1):
    # 거리 정보가 k이면 
    if visited[i] == k: 
        # 현재 도시 번호 print 
        print(i)
        # k인 도시 존재 여부 True
        k_exist = True 

# 거리가k인 도시가 없으면
if not k_exist: 
    # -1 print 
    print(-1)