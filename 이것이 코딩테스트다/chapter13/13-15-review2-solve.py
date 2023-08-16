"""
1번부터 n번까지 도시, m개의 단방향 도로 존재
모든 도로 거리 1
특정한 도시 x로부터 출발하여 도달할 수 있는 모든 도시중
최단거리가 정확히 k인 모든 도시들의 번호 출력
x에서 x로 가는 최단거리 항상 0

"""
# sys import
import sys 
# input을 빠른 입력으로 변경 
input = sys.stdin.readline

# 도시 개수 n, 도로 개수 m, 거리정보 k, 출발 도시 번호 x 주어짐
n, m, k, x = map(int, input().split())
# 각 도시에 연결된 도시들을 저장하는 graph []를 원소로 (n + 1)개의 리스트로 생성
graph = [[] for _ in range(n + 1)]
# m번을 반복하면서
for _ in range(m):
    # a, b 입력 (a번 도시에서 b번 도시로 이동하는 단방향 도로 존재)
    a, b = map(int, input().split())
    # graph[a]에 b 삽입
    graph[a].append(b) 
# 방문 여부 확인하는 visited 리스트 : -1를 원소로 (n + 1) 길이 리스트로 생성 
visited = [-1] * (n + 1)
    
# deque import 
from collections import deque
# bfs 선언 : 매개변수 start 
def bfs(start):
    # 큐 q deque로 선언 
    q = deque()
    # q에 start 삽입 
    q.append(start)
    # visited[start]를 0으로 변경 
    visited[start] = 0
    
    # 큐가 빌때까지 반복하면서
    while q: 
        # 큐에서 popleft하여 현재 도시 위치 now 
        now = q.popleft() 
        # 다음 거리 next_dist 는 visitd[now] + 1 
        next_dist = visited[now] + 1
        
        # graph[now]]와 연결된 도시들을 하나씩 확인하면서 : 원소 next_city
        for next_city in graph[now]:
            # visited[next_city]가 -1이면(방문하지 않았으면) 
            if visited[next_city] == -1:
                # q에 next_city 삽입
                q.append(next_city)
                # visited[next_city]는 next_dist
                visited[next_city] = next_dist 

# bfs(x) 호출 
bfs(x)
    
# x로부터 출발하여 도달할 수 있는 도시중 최단거리가 k인 모든 도시번호 한줄에 하나씩 오름차순 출력
# 최단거리 k인 도시가 하나도 존재하지 않으면 -1 
# k가 visited안에 없으면
if k not in visited:
    # -1 출력 
    print(-1)

# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1):
    # visited[i]가 k이면
    if visited[i] == k:
        # i 출력
        print(i)