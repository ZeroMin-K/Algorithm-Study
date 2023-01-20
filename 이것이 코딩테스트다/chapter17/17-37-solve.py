"""
n개의 도시
한 도시에 출발하여 다른 도시에 도착하는 m개의 버스 
각 버스는 한번 사용할때마다 비용있음
A -> B로 가는데 비용 최솟값 계산
2 <= n <= 100
1 <= m <= 100,000

도시의 개수 => 노드의 개수. 노드의개수가 적고
모든 도시에서 모든 도시로 도착하는 경우의수 출력 => 플로이드 워셜 알고리즘 필요 
"""
import sys
input = sys.stdin.readline

INF = int(1e9) 

# 도시의 개수 n 입력
n = int(input())

# 2차원 도시 리스트 생성 
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기자신에서 자기자신으로 도착할때는 비용 0 
for i in range(1, n + 1):
    graph[i][i] = 0

# 버스의 개수 m 입력
m = int(input())
# m 번반복하며
for _ in range(m):
    # 버스 시작도시 a, 도착도시 b, 비용 c 입력 
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)


# 플로이드 워셜 알고리즘 
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b]) 

# n개의 줄 출력 
# i번째 줄 도시 i에서 j번째 숫자 j로 가는 최소 비용 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] >= INF:
            # 갈 수 없으면 0 출력
            print(0, end =' ')
        else:
            print(graph[i][j], end =' ')
            
    print()