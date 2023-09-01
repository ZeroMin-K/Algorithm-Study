"""
1 ~ n번까지 헛간 중 하나에 골라 숨음
술래는 항상 1번 헛간에서 출발
맵에는 총 m개의 양방향 통로 존재. 하나의 통로는 서로 다른 두 헛간 연결
항상 어떤 헛간에서 다른 헛간으로 도달 가능한 형태
1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단
최단거리의 의미는 지나야하는 길의 최소 개수
숨을 헛간의 번호 출력 
숨어야하는 헛간번호가 여러개면 가장 작은 헛간번호 출력
헛간번호, 헛간거리, 같은 헛간개수 출력 
"""
import heapq 
INF = int(1e9) 
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1) 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 
    
def dijkstra(start):
    q = [] 
    distance[start] = 0  
    heapq.heappush(q, (distance[start], start)) 
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for next in graph[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))

dijkstra(1)

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
        
print(max_node, max_distance, len(result))