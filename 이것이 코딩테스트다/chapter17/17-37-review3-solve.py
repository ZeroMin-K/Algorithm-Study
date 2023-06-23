"""
n개의 도시(2 <= n <= 100)
한 도시에서 다른 도시 도착하는 m개의 버스 (1 <= m <= 100,000)
버스 한번사용할때마다 비용듬
모든 도시 쌍 (a, b)에 대해 도시 a에서 b로가는데 필요한 비용 최솟값 구함

모든 도시 쌍, 최대 100개도시, 경로 비용 계산 => 플로이드 워셜 알고리즘 사용 
시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있으니 입력할 때마다 가장 최소경로를 저장하기 
"""

# 빠른 입력을 위해 input 메서드 변경
import sys
input = sys.stdin.readline

# 도달할 수 없는 거리 INF를 1e9로 지정 
INF = int(1e9) 

# 도시 개수 n 입력
n = int(input()) 
# 도시를 2차원 인접행렬식으로 (n + 1) * (n + 1) 의 값은 INF로 초기화한 2차원 리스트 graph
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 버스 개수 m 입력
m = int(input()) 
# m번 반복하면서 
for _ in range(m): 
    # 시작 도시 a, 도착 도시 b, 비용 c를 입력받아 int로 map
    a, b, c = map(int, input().split())
    # graph[a][b]는 graph[a][b], c중 작은 값으로 저장
    graph[a][b] = min(graph[a][b], c)

# -- 자기자신에 대한 경로는 0으로 초기화 --
# 인덱스 k: 1부터 n까지 반복하면서
for k in range(1, n + 1):
    # graph[k][k] 의 값은 0 
    graph[k][k] = 0

# -- 플로이드 워셜 알고리즘 진행 --
# 인덱스 k: 1부터 n까지 반복하면서
for k in range(1, n + 1):
    # 인덱스 a: 1부터 n까지 반복하면서
    for a in range(1, n + 1):
        # 인덱스 b: 1부터 n까지 반복하면서
        for b in range(1, n + 1):
            # graph[a][b]의 값은 graph[a][b]와 graph[a][k] + graph[k][b] 값 중 작은 것
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1):
    # 인덱스 j: 1부터 n까지 반복하면서
    for j in range(1, n + 1):
        # graph[i][j] 가 INF이면 (도달할 수 없으면)
        if graph[i][j] == INF: 
            # 0 출력. print의 end는 공백
            print(0, end = ' ')
        # 나머지의 경우 
        else: 
            # graph[i][j] 출력. print의 end는 공백
            print(graph[i][j], end = ' ')
    # 한줄띄우기 
    print()

