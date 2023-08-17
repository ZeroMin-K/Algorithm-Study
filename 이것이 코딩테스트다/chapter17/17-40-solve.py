"""
1 ~ n번까지 헛간 중 하나 골라서 숨기
술래는 항상 1번 헛간에서 출발
총 m개의 양방향 통로 존재. 서로 다른 두헛간연결 
1번 헛간으로부터 최단거리가 가장 먼 헛간이 가장 안전하다고 판단
숨을 헛간의 번호를 출력 

n이 크기 때문에 다익스트라 알고리즘을 활용하여 1번헛간으로부터 시작해
각 n번까지 헛간들의 최단거리를 계산하고 그중 가장 큰값을 출력하기 
"""

import sys
import heapq 

input = sys.stdin.readline
INF = int(1e9)

#  n, m 입력
n, m = map(int, input().split())
# 헛간들의 연결정보를 저장하는 2차원 리스트 graph 빈 리스트를 원소로하여 (n + 1)길이로 초기화 
graph = [[] for _ in range(n + 1)]
# 각 헛간들의 최단 거리를 저장하는 distance INF를 원소로하여 (n + 1) 길이로 초기화 
distance = [INF] * (n + 1) 
# m번 반복하면서
for _ in range(m):
    # a, b 입력
    a, b = map(int, input().split())
    # graph[a]에 b 삽입
    graph[a].append(b)
    # graph[b]에 a 삽입
    graph[b].append(a) 

# q 생성
q = [] 
# q에 (0, 1) 삽입 비용, 노드번호
q.append((0, 1))
# distance[1] 은 0으로 값 변경
distance[1] = 0

# q가 빌 때까지 반복하면서  
while q: 
    # dist, node 를 q에서부터 heappop함 
    dist, node = heapq.heappop(q) 

    # distace[node]가 dist보다 작다면
    if distance[node] < dist: 
        # continue
        continue 

    # 다음 노드까지 비용 cost 는 dist + 1
    cost = dist + 1
    # graph[node]를 하나씩 탐색하면서 : 원소 next
    for next in graph[node]:
        # cost가 distance[next]보다 작으면
        if cost < distance[next]: 
            # distance[next]는 cost로 값 변경
            distance[next] = cost
            # q에 (cost, next)를 heappush
            heapq.heappush(q, (cost, next))

# 최단거리가 가장 먼 헛간거리 max_dist 0으로 초기화
max_dist = 0
# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1):
    # distance[i]가 INF가 아니고 distance[i]가 max_dist보다 크면
    if distance[i] != INF and distance[i] > max_dist: 
        # max_dist 는 distance[i]로 초기화 
        max_dist = distance[i] 

# 최초 헛간 번호 first 0
# 같은 헛간 개수 same 0
# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1):
    if distance[i] == max_dist:
        first = i
        break

print(first, distance[first], distance.count(distance[first]))
