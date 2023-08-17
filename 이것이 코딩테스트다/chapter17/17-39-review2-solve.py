import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(int(input())):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]

    q = []
    q.append((graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    while q: 
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue 

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n - 1][n - 1])