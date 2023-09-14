"""
가충치 없는 방향 그래프 g
모든 정점(i, j)에 대해 i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하기

플로이드 워셜을 통해서 각 그래프에서 그래프로 가는 거 구하기 
"""
import sys
input = sys.stdin.readline
INF = int(1e9) 

# 정점의 개수 n 입력
n = int(input())
graph = [] 
# n번 반복하며 
for _ in range(n): 
    # 인접그래프 행렬입력 (i 번째 줄의 j번째 숫자가 1인 경우 간선 존재)
    data = list(map(int, input().split()))
    for i in range(n):
        if data[i] == 0:
            data[i] = INF
    graph.append(data)

# 자기자신으로 가는 비용은 0으로 초기화
for k in range(n):
    graph[k][k] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b] + 1) 

# n개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력
# 경로가 있으면 1, 없으면 0출력 
for i in range(n):
    for j in range(n):
        if graph[i][j] >= INF:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()