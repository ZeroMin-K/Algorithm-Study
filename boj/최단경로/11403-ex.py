import sys
input = sys.stdin.readline

# 정점의 개수 n 입력
n = int(input())
graph = [] 
# n번 반복하며 
for _ in range(n): 
    graph.append(list(map(int, input().split())))

# 자기자신으로 가는 비용은 0으로 초기화
for k in range(n):
    graph[k][k] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][k] == 1 and graph[k][b] == 1):
                graph[a][b] = 1

# n개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력
# 경로가 있으면 1, 없으면 0출력 
for i in range(n):
    for j in range(n):
        print(graph[i][j], end = ' ')
    print()