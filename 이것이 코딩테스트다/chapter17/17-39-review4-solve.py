"""
출발지점에서 목표지점까지 이동할때 최적경로 찾도록 개발
n * n 크기 2차원 공간. 각 칸 지나는 비용존재
가장 왼쪽 위칸 [0][0]위치에서 가장 오른쪽 아래칸 [n- 1][n- 1]위치로 이동하는 최소 비용
상, 하, 좌, 우 인접한 곳으로 1칸씩 이동 가능 
"""

# heapq import
import heapq 
# INF 선언 
INF = int(1e9) 

# 상, 하, 좌우에 대한 움직임 리스트 moves 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# dijkstra 함수 선언 : 매개변수 graph, distance
def dijkstra(n, graph, distance):
    # 시작위치 start_x, start_y = 0, 0
    start_x, start_y = 0, 0 
    # 큐 q 빈리스트로 생성 
    q = [] 
    distance[start_x][start_y] = graph[start_x][start_y]
    # q에 (0, start_x, start_y) heappush
    heapq.heappush(q, (distance[start_x][start_y], start_x, start_y))
    
    # q가 빌때까지 반복
    while q: 
        # dist, x, y 는 q에서 heappop한것 
        dist, x, y = heapq.heappop(q)
        # distance[x][y]가 dist보다 작으면
        if distance[x][y] < dist: 
            # continue
            continue
            
        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves: 
            # nx는 x + move[0]
            nx = x + move[0] 
            # ny는 y + move[1]
            ny = y + move[1] 
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            # cost 는 dist + graph[nx][ny]
            cost = dist + graph[nx][ny] 
            # distance[nx][ny]보다 cost가 작으면
            if distance[nx][ny] > cost: 
                # distance[nx][ny] 는 cost로 갱신
                distance[nx][ny] = cost 
                # q에 (cost, nx, ny) heappush 
                heapq.heappush(q, (cost, nx, ny))

# 테스트케이스 t 입력
t = int(input()) 
# t번씩 반복하면서 
for _ in range(t): 
    # 탐사공간의 크기 n 입력 
    n = int(input())
    # 탐사공간 graph 빈 리스트로 생성 
    graph = [] 
    # n번 반복하면서 
    for _ in range(n): 
        # 각 탐사 비용 공백구분으로 입력 
        graph.append(list(map(int, input().split())))
        
    # 각 비용에 대한 2차원 리스트 [INF] * n n으로 초기화 
    distance = [[INF] * n for _ in range(n)]
    # dijkstrsa 호출 : graph, distance 
    dijkstra(n, graph, distance)
    
    # distance[n - 1][n - 1] 출력 
    print(distance[n - 1][n - 1])