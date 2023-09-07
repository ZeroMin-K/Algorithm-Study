"""
출발지점에서 목표지점까지 이동할때 항상 최적경로 찾기
n * n 크기 2차원 공간. 각 칸 지나기위한 비용 존재
[0][0] 위치에서 [n - 1][n- 1]위치로 이동하는 최소 비용 출력
상, 하, 좌, 우 인접한 곳으로 1칸씩 이동 가능 
"""
# heapq import 
import heapq 
# INF 무한대로 설정
INF = int(1e9) 

# 상, 하, 좌, 우 움직임에 대한 움직임 리스트 moves 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 테스트 케이스 수 t 입력
t = int(input()) 
# t번 반복하면서 
for _ in range(t): 
    # 탐사 공간의 크기 n 입력 
    n = int(input()) 
    # 현재 탐사공간 graph 빈리스트로 초기화 
    graph = [] 
    # n번 반복하면서 
    for _ in range(n): 
        # 탐사공간 크기 입력하여 graph에 삽입
        graph.append(list(map(int, input().split())))

    # 현재 탐사공간에대한 거리 리스트 distance n * n 크기 값은 INF로 초기화 
    distance = [[INF] * n for _ in range(n)]

    # 큐 q 빈리스트로 생성
    q = [] 
    # distance[0][0]의 값은 graph[0][0]
    distance[0][0] = graph[0][0] 
    # q에 (distance[0][0], 0, 0) heappush 
    heapq.heappush(q, (distance[0][0], 0, 0))

    # 큐가 빌 때까지 반복 
    while q: 
        # cost, x, y를 q에서 heappop
        cost, x, y = heapq.heappop(q) 
        # distance[x][y]가 cost보다 작으면
        if distance[x][y] < cost: 
            # continue 
            continue 
        
        # moves를 하나씩 탐색하면서 : 원소 move 
        for move in moves: 
            # nx, ny는 x + move[0], y + move[1]
            nx, ny = x + move[0], y + move[1] 

            # nx, ny가 0보다 작거나 n보다 같거나 크면 
            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                # continue 
                continue 

            # [nx][ny]까지의 비용 dist는 cost + graph[nx][ny] 
            dist = cost + graph[nx][ny]
            # distance[nx][ny]가 dist보다 크면
            if distance[nx][ny] > dist: 
                # dinstance[nx][ny]는 dist
                distance[nx][ny] = dist 
                # q에 dist, nx, ny heappush 
                heapq.heappush(q, (dist, nx, ny)) 

    # distance[n - 1][n- 1] 출력 
    print(distance[n - 1][n - 1])

