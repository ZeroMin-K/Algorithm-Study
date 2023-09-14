"""
방향 그래프 
주어진 시작점에서 다른 모든 정점으로 최단경로 구하는 프로그램

플로이드 워셜로 구하기에는 노드수가 많음
다익스트라 사용하여 풀이 

"""
# 빠른 입력 
import sys
input = sys.stdin.readline
# INF 정의 
INF = int(1e9) 

# 정점개수 v, 간선 개수 e입력
v, e = map(int, input().split())
# 시작정점이 번호 k입력 
k = int(input())
# 정점에 연결정보를 기록하는 2차원 리스트 빈리스트를 원소로하여 길이가 v + 1인 graph 생성
graph = [[] for _ in range(v + 1)]
# e만큼 반복하면서
for _ in range(e): 
    # u, v, w입력 u에서 v로가는 가중치 w인 간선 존재 
    u, ver, w = map(int, input().split())
    graph[u].append((ver, w))

# 거리 테이블
distance = [INF] * (v + 1)

import heapq 

# 다익스트라 알고리즘 함수 선언
def dijkstra(start):
    q = [] 
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = dist + next[1]
            next_node = next[0]

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))

# 시작정점 k로부터 다익스트라 알고리즘 수행  
dijkstra(k)

# v개줄에 걸쳐 i번째 줄에 i번 정점으로 최단경로 값 출력
# 시작점 자신은 0출력, 경로 존재하지 않는 경우 INF 출력 
for i in range(1, v + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])