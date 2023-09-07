"""
n개의 도시. 
한도시에 출발하여 다른 도시에 도착하는 m개의 버스 
각 버스 사용 비용있음
모든도시에 대해 비용의 최솟값 게산

"""
# 빠른입력
import sys
input = sys.stdin.readline
# 무한대거리 INF
INF = int(1e9) 

# 도시 개수 n 입력
n = int(input())
# 버스 개수 m 입력
m = int(input()) 
# 각 그래프 graph 빈 리스트로 (n + 1) 길이
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신으로 가는 비용은 0으로 초기화 
for i in range(1, n + 1): 
    graph[i][i] = 0

# m번 반복하면서
for _ in range(m): 
    # 버스 정보 주어짐. 버스 시작도시 a, 도착도시 b, 비용 c
    a, b, c = map(int, input().split()) 
    # 노선이 하나가 아닐 수 있으니 작은 값으로 변경 
    graph[a][b] = min(graph[a][b], c)

# 인덱스 k: 1부터 n까지 반복하면서
for k in range(1, n + 1):
    # 인덱스 i: 1부터 n까지 반복하면서
    for i in range(1, n + 1): 
        # 인덱스 j: 1부터 n까지 반복하면서
        for j in range(1, n + 1): 
            # dp[i][j] 는 dp[i][j], dp[i][k] + dp[k][i] 중 작은거로 설정
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1): 
    # 인덱스 j: 1부터 n까지 반복하면서
    for j in range(1, n + 1): 
        # dp[i][j]가 INF보다 같거나 크면
        if graph[i][j] >= INF:
            # 0 출력 end 공백
            print(0, end = ' ') 
        # 나머지 경우 
        else: 
            # dp[i][j] 출력 end는 공백
            print(graph[i][j], end = ' ')
    # 한 줄 넘어가기 
    print()
