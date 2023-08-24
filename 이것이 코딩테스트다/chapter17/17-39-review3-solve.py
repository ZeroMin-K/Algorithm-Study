"""
출발지점에서 목표지점까지 이동할때 최적의 경로 찾기
n * n 크기 2차원 공간. 각 칸을 지나기 위한 비용 존재
[0][0] 위치에서 [n - 1][n-  1]위치로 이동하는 최소 비용 출력 
특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동 가능 
"""
# heapq import 
import heapq 

INF = int(1e9) 

# 테스트 케이스 수 t 입력
t = int(input())

# 상, 하, 좌, 우로 움직이는 x,y좌표 리스트 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 다익스트라 함수 선언 
def dijkstra(n, graph, distance, start_x, start_y): 
    # 힙큐 q 생성
    q = [] 
    # 시작위치 큐에 힙푸쉬
    heapq.heappush(q, (graph[start_x][start_y], start_x, start_y))
    # 현재 시작위치에서 거리
    distance[0][0] = graph[0][0] 

    # q가 빌때까지 반복
    while q: 
        # dist, x, y 는 q에서 뺌
        dist, x, y = heapq.heappop(q) 

        # distanc[x][y]가 dist보다 작으면
        if distance[x][y] < dist: 
            # 반복 진행
            continue 

        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves: 
            # 다음좌표 nx는 x + move[0]
            nx = x + move[0] 
            # 다음좌표 ny는 y + move[1]
            ny = y + move[1] 

            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                continue

            # (nx, ny)까지 비용 cost는 dist + graph[nx][ny]
            cost = dist + graph[nx][ny] 
            # distance[nx][ny]보다 cost가 작으면
            if cost < distance[nx][ny]: 
                # distance[nx][ny] = cost로 갱신
                distance[nx][ny] = cost 
                # 큐에 cost, x, y 힙푸쉬 
                heapq.heappush(q, (cost, nx, ny))

# t번 반복하면서
for _ in range(t): 
    # 탐사공간 크기 n 입력 
    n = int(input())
    # 탐사 공간에 대한 2차원 리스트 graph 빈리스트로 생성 
    graph = [] 
    # 거리 리스트 
    distance = [[INF] * n for _ in range(n)]

    # n번 반복하면서
    for _ in range(n): 
        # 각 칸에 대한 비용 존재 공백으로 구분하여 graph에 삽입 
        graph.append(list(map(int, input().split())))

    # dijkstra 호출 
    dijkstra(n, graph, distance, 0, 0)

    
    # [0][0] 위치에서 [n- 1][n - 1]의 위치로 이동하는 최소 비용을 출력 
    print(distance[n - 1][n - 1])