import sys
input = sys.stdin.readline

INF = int(1e9)      # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수 입력
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현) 생성. 모든값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신에서 자기자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아 그값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우 0 출력
        if graph[a][b] == INF:
            print(0, end=' ')
        # 도달할 수 없는 경우 거맃 ㅜㄹ력
        else:
            print(graph[a][b], end = " ")
    print()