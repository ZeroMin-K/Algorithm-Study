"""
n개의 도시. 다른 도시에 도착하는 m개의 버스 
한번 사용할때 비용 있음
모든 도시 쌍 (a, b)에 대해 a에서 b로가는 필요한 비용 최솟값 구하기

모든 쌍, 최대 100개의도시 => 플로이드 워셜을 사용하여 풀이 
"""

# 빠른 입력
import sys
input = sys.stdin.readline

# 도달할수없는 경우에 대해 무한값 지정 
INF = int(1e9)

# 도시 개수 n입력
n = int(input())
# 버스 개수 m 입력
m = int(input())

# 각 도시들 연결정보 기록하는 2차원 리스트 그래프
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# m번 반복하면서 
for _ in range(m):
    # 시작도시 a, 도착도시 b, 비용 c 입력
    a, b, c = map(int, input().split())
    # 노선이 하나아닐수있으니 최소값을 저장 
    graph[a][b] = min(graph[a][b], c)
    

# 자기자신에게 가는 비용은 0을 초기화 
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘 수행
# 인덱스 k: 1부터 n까지 반복하면서
for k in range(1, n + 1):
    # 인덱스 i: 1부터 n까지 반복하면서
    for i in range(1, n + 1):
        # 인덱스 j: 1 부터 n까지 반복하면서 
        for j in range(1, n + 1):
            # i에서 j까지 가는거리 [i][j]는 [i][j]와 [i][k], [k][j] 거리 더한거중 최소 거리
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1):
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(1, n + 1):
        # 도달 할 수없으면 
        if graph[i][j] == INF:
            # 0 출력, end = ' '
            print(0, end = ' ')
        # 있으면 
        else:
            # [i][j] 최단 경로 print. end = ' '
            print(graph[i][j], end = ' ')
    # 한 줄 넘어가기 
    print()