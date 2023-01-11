from collections import deque
import sys
input = sys.stdin.readline


# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발도시 번호 x
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

# m번 반복하며
for _ in range(m):
    # a, b 입력. a번 도시로에서 b번 도시로 이동하는 단방향 도로가 존재 
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * (n + 1)

def bfs(start, visited):
    q = deque()
    q.append((start, 0))
    visited[start] = -1

    while q:
        now, dist = q.popleft()

        for next in graph[now]:
            if visited[next] == 0:
                q.append((next, dist + 1))
                visited[next] = dist + 1

bfs(x, visited)
check = False
# x로부터 출발하여 도달할 수 있는 도시중에서 
for i in range(1, n + 1):
    # 최단거리가 k인 모든 도시 번호를 한줄에 하나씩 오름차순으로 출력
    if visited[i] == k:
        print(i)
        check = True

# 존재하지 않으면 -1 출력
if not check: 
    print(-1)