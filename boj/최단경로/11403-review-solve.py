"""
가중치 없는 방향 그래프 G
모든 정점 i, j에서 i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 계산

모든 정점 100 * 100 => 플로이드 워셜 알고리즘 
"""

import sys
input = sys.stdin.readline 

# 정점의 개수 n 입력
n = int(input()) 
graph = [] 
# n번 반복하면서 
for _ in range(n): 
    # 인접행렬 한줄 입력
    graph.append(list(map(int, input().split())))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1


# n개의 줄에 걸쳐서 인접행렬 출력 
for i in range(n):
    for j in range(n):
        print(graph[i][j], end = ' ')
    print()