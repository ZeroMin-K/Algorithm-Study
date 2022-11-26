"""
1번부터 N번까지 회사 - 회사끼리 서로 도로 통해 연결
1번회사에 위치해 X번 회사에 방문해 물건 판매
회사끼리 연결된 도로 통해 양방향 이동. 1만큼 시간으로 이동
1번회사 -> K번 회사 -> X번 회사 방문 
최소시간계산 - 도달 불가시 -1 출력

1 <= 회사, 경로 개수 <= 100 
플로이드 워셜 사용 가능
1번에서 k번까지 가는 최소경로 + k번에서 x번까지 가는 최소 경로  
"""
import sys
input = sys.stdin.readline

INF = int(1e9)

# 회사 개수 n,  경로 개수 m 입력
n, m = map(int, input().split())

# 모든 경로를 담고 있는 2차원 리스트 그래프 생성 - 무한으로 초기화 
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기자신으로 가는 경로는 0으로 초기화 
for i in range(1, n + 1):
    graph[i][i] = 0

# m번 반복하며
for _ in range(m):
    # 연결된 회사 번호 a, b 입력 - a에서 b로 가는 경로는 1. 양방향 
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 플로이드 워셜 알고리즘 
# k를 1부터 n까지 반복하면서 (중간 경유)
for k in range(1, n + 1):
    # i를 1부터 n까지 반복하면서 (출발 회사)
    for i in range(1, n + 1):
        # j를 1부터 n까지 반복하면서 (도착 회사)
        for j in range(1, n + 1):
            # i에서 j까지 가는 경로 = i,k + k,j경로, i,j 경로 둘중 최소 경로 
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# x, k 입력 
x, k = map(int, input().split())

# 1 -> k  -> x 거리 [1][k] + [k][x]
distance = graph[1][k] + graph[k][x]
# x나 k로 가는 경로가 존재하지 않으면
if distance >= INF:
    # -1 출력
    print(-1)
# 경로가 존재하면
else:
    # 거리  출력 
    print(distance)