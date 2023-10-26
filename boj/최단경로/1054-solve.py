"""
방향성이 없는 그래프. 1번 정점에서 n번 정점으로 최단거리 이동
임의로 주어진 두 정점은 반드시 통과 
한번 이동했던 정점, 간선도 다시 이동가능
최단 경로로 이동해야함
1번정점에서 n번정점으로 이동시 두정점을 반드시 거치면서 최단경로 이동하는 프로그램

1 -> v1 -> v2 -> n까지 도착하는것과 
    1 -> v2 -> v1 -> n까지 도착하는 것 중 최단 경로 찾기 

1. 1 -> v1까지 최단경로 + v1 -> v2까지 최단경로 + v2 -> n까지 최단 경로 
2. 1 -> v2까지 최단 경로 + v2 -> v1까지 최단 경로 + v1 -> n까지 최단경로 

1. 1에서 출발할때 v1, v2까지 최단 거리 
2. v1에서 출발 할 때 v2, n까지 최단 거리
3. v2에서 출발 할대 v1, n까지 최단 거리 찾기 

[출발노드, 1번 경로, 2번 경로]
    1, v1, v2
    v1, v2, n
    v2, n, v1
각 경로에 대해 최단경로 찾기 
"""

# 빠른 입력 
import sys
input = sys.stdin.readline
# 거리가 무한인경우 INF
INF = int(1e9) 

# 정점의 개수 n, 간선의 개수 e 입력
n, e = map(int, input().split())

# 정점에 대한 그래프 생성
graph = [[] for _ in range(n + 1)]

# e번 반복하면서 
for _ in range(e): 
    # a, b, c 입력 : a번 정점에서 b정점까지 양방향 길 존재. 거리 c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
# 반드시 거쳐야하는 서로 다른 정점 v1, v2 입력
v1, v2 = map(int, input().split())

# heapq import 
import heapq 
# 다익스트라 알고리즘 함수 선언 : 매개변수 start, distance
def dijkstra(start, distance): 
    # 큐 q 생성 
    q = [] 
    # 시작 정점 start는 거리 0 
    distance[start] = 0 
    # (0, start)를 q에 push 
    heapq.heappush(q, (distance[start], start))

    # 큐가 빌 때까지 반복 
    while q: 
        # 현재 정점 node, 거리 dist는 q에서 pop한 것
        dist, node = heapq.heappop(q) 

        # 현재 node까지 거리인 distance[node]가 dist보다 작으면
        if distance[node] < dist: 
            # continue
            continue 

        # node와 연결된 정점들을 확인하면서 : graph[node] 반복 원소 next
        for next in graph[node]: 
            # 다음 노드 next_node는 next[0]
            next_node = next[0] 
            # 다음 노드까지 거리 next_cost는 dist + next[1] 
            next_cost = dist + next[1] 

            # next_node까지 거리 dinstace[next_node]가 다음 노드까지 거리 next_cost보다 크면
            if next_cost < distance[next_node]: 
                # distance[next_node]는 next_cost
                distance[next_node] = next_cost 
                # (next_cost, next_node)를 q에 삽입 
                heapq.heappush(q, (next_cost, next_node))

# routes [1, v1, v2], [v1, v2, n], [v2, n, v1] 
routes = [[1, v1, v2], [v1, v2, n], [v2, n, v1]]
# 최단경로 min_dists 0, 0, 0
min_dist = [0] * 3

# routes를 하나씩 반복하면서 : route 
for route in routes: 
    # 1번 정점에서 n번 정점까지 최단 경로 테이블 distance : 원소는 INF n + 1 길이로 초기화 
    distance = [INF] * (n + 1) 
    # route[0]에서 출발하여 다익스트라 알고리즘 수행
    dijkstra(route[0], distance)
    # 인덱스 i: 1부터 2까지 반복하며 
    for i in range(1, 3): 
        # min_dist[i]에 distance[route[i]] 더함
        min_dist[i] += distance[route[i]]

# 최단 경로 길이 출력. 경로가 없으면 -1 출력 
# min_idst[1]과 [2]둘다 INF보다 크면 -1 출력, 아니면 작은 것출력
print(-1 if min_dist[1] >= INF and min_dist[2] >= INF else min(min_dist[1], min_dist[2]))