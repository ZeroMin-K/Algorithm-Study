"""
방향 그래프가 주어지면 모든정점으로의 최단 경로 계산하기

정점의 개수 20,000 => 다익스트라 사용하기 

"""
INF = int(1e9) 

import sys
input = sys.stdin.readline

# 정점의 개수 v, 간선의 개수 e 입력
v, e = map(int, input().split())
# 시작 정점 번호 k 입력
k = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

# e번 반복하면서
for _ in range(e): 
    # u, v, w 입력 - u에서 v로 가는 가중치 w인 간선 존재 (서로 다른 두 정점사이에여러개 간선 존재 가능)
    u, n, w = map(int, input().split())

    graph[u].append((n, w))
    
import heapq
def dijkstra(start):
    q = [] 
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

# v개 줄에 걸쳐 i번째 줄에 i번 정점으로 최단 경로값 출력 - 시작점 0, 경로 존재하지 않을 때 INF 출력 
for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])