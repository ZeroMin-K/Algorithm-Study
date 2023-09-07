"""
술래로부터 숨을 곳 찾기 
1 ~ n번까지 헛간중 하나 골라서 숨음
술래는 항상 1번 헛간에서 출발
m개의 양방향 통로 존재. 하나의 통로는 서로 두 헛간연결
전체 맵은 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태 
1번 헛간으로부터 최단거리가 가장 먼 헛간이 가장 안전하다고 판단
최단거리: 지나야하는길의 최소 갯수 
동빈이가 숨을 헛간의 번호 출력 
"""
# heapq import 
import heapq 
# 무한대 INF 선언 
INF = int(1e9) 
# n, m 입력
n, m = map(int, input().split())
# 각 헛간 그래프 graph 빈리스트를 원소로 n + 1길이로 초기화 
graph = [[] for _ in range(n + 1)]
# m번 반복하면서 
for _ in range(m): 
    #  a, b 입력
    a, b = map(int, input().split())
    # graph[a]에 (b, 1) 삽입
    graph[a].append((b, 1)) 
    # graph[b]에 (a, 1) 삽입
    graph[b].append((a, 1))  

# 각 거리 테이블 distance INF로 n + 1 길이로 초기화 
distance = [INF] * (n + 1) 

# 큐 q생성
q = [] 
# distance[1] 0으로 초기화 
distance[1] = 0 
# 큐에 (distance[1], 1) heappush 
heapq.heappush(q, (distance[1], 1))

# q가 빌때까지 반복하면서 
while q: 
    # dist, now는 q에서 heappop한 값
    dist, now = heapq.heappop(q) 
    # dist가 distance[now]보다 크면
    if dist > distance[now]: 
        # continue
        continue 
    
    # graph[now]를 하나씩 반복하면서: next
    for next in graph[now]: 
        # 다음 노드 next_node 는 next[0] 
        next_node = next[0] 
        # 다음 노드까지 거리 cost는 dist + next[1]
        cost = dist + next[1] 
        # cost가 distance[next_node]보다 작으면
        if cost < distance[next_node]: 
            # distance[next_node]는 cost로 갱신
            distance[next_node] = cost
            # q에 (cost, next_node) heap push 
            heapq.heappush(q, (cost, next_node))

# 가장 먼거리 far_dist 0으로 초기화 
far_dist = 0 
result = [] 
# 인덱스 i: 1부터 n까지 반복하면서 
for i in range(1, n + 1): 
    # far_dist보다 distance[i]가 더 크면
    if far_dist < distance[i]: 
        # far_dist는 distance[i]
        far_dist = distance[i] 
        # result는 [i]
        result = [i] 
    # far_dist와 distance[i]가 같으면
    elif far_dist == distance[i]: 
        # result에 i 삽입 
        result.append(i)

# 숨어야하는 헛간번호 (만약 거리가 같은 헛간이 여러개면 가장 작은 헛간번호 출력), 헛간거리, 같은 헛간개수 출력 
print(result[0], far_dist, len(result))