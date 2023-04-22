"""
1번부터 n번까지의 도시, m개의 단방향 도로. 모든 도로거리 1
특정 도시 x로부터 도달할 수 있는 모든 도시중 최단거리가 정확히 k인 모든 도시들의 번호 출력
x에서 x까지 거리는 항상 0

각 도로 거리는 값이 다르지 않고 전부 1이기때문에 bfs를 이용하여 해당 위치까지 거리를 더해주고 
거리가 k인 도시들 찾기 
"""

# deque import 
from collections import deque
# 빠른 입력을 위한 input 메서드 변경
import sys
input = sys.stdin.readline

# 도시 개수 n, 도로 개수 m, 거리정보 k, 출발 도시번호 x입력
n, m, k, x = map(int, input().split())

# 각 도시와 도로에 해당하는 리스트 graph 초기화 (빈 리스트를 원소로 갖으며 (n + 1) 길이의 리스트 )
graph = [[] for _ in range(n + 1)]
# m번 반복하면서 
for _ in range(m):
    # a, b 입력 - a번 도시에서 b번도시로 이동가능
    a, b = map(int, input().split())
    # graph[a]에 b를 append
    graph[a].append(b)
    
# 각 거리 정보를 저장하는 distance 리스트 - (n + 1)길이의 -1 로 초기화
distance = [-1] * (n + 1)

# bfs 선언 - 매개변수 x 출발도시 
def bfs(x):
    # 큐 선언
    q = deque()
    # 큐에 출발도시 x append
    q.append(x)
    # 출발도시 x는 distance에서 거리는 0으로 초기화
    distance[x] = 0
    
    # 큐가 빌때까지 반복 
    while q: 
        # 큐에서 현재 도시 입력
        now = q.popleft()
        
        # graph[현재도시]에서 연결된 도로들을 하나씩 탐색하면서 
        for next in graph[now]:
            # 다음 도시를 방문하지 않으면(distance가 -1이면)
            if distance[next] == -1:
                # 다음도시의 거리는 현재도시에서 거리 + 1
                distance[next] = distance[now] + 1
                # 다음 도시를 큐에 넣음 
                q.append(next)
                
# 출발도시 x를 인자로 bfs 호출
bfs(x)

# 최단거리k인 도시가 존재하는지 여부 check = False
check = False
# 인덱스 i를 1부터 n 까지 반복하면서    
for i in range(1, n + 1):
    # distance[i]가 k이면
    if distance[i] == k:
        # i 출력
        print(i)
        # check = True로 존재하는여부 확인
        check = True
        
# check가 False이면
if not check: 
    # -1 출력 
    print(-1)