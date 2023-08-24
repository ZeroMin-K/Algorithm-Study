"""
n개의 도시 
한 도시에서 출발하여 다른 도시에 도착하는 m개버스
각 버스는 한번 사용할때 필요한 비용이 있음
모든 도시 (a, b)에 대해 도시 a에서 b로가는데 필요한 비용의 최솟값 구함 

도시가 연결, 연결된 도시로 가는데 최소비용 => 최단경로
n이 100개 이하, 모든 비용 => 플로이드워셜 사용
"""
# sys import
import sys
# input을 빠른 입력으로 변경 
input = sys.stdin.readline

# 이동할 수 없는 경우에 대해 INF값 설정 
INF = int(1e9) 

# 도시 개수 n입력
n = int(input()) 
# 버스 개수 m 입력
m = int(input())

# 각 도시에 거리정보를 담는 2차원 리스트 distance INF를 값으로 n * n 크기로 변경 
distance = [[INF] * (n + 1) for _ in range(n + 1)]

# m번 반복하면서 
for _ in range(m): 
    # a, b, c 입력 (시작도시 a, 도착 도시 b, 비용 c)
    a, b, c = map(int, input().split()) 
    # distance[a][b]가 c보다 크면
    if distance[a][b] > c: 
        # distance[a][b]는 c로 값 초기화 
        distance[a][b] = c

# 인덱스 i: 0부터 n - 1까지
for i in range(1, n + 1): 
    # dinstace[i][i] 0으로 초기화 
    distance[i][i] = 0

# << 플로이드 워셜 알고리즘 수행 >> 
# 인덱스 k: 0부터 n -1 까지 반복하면서
for k in range(1, n + 1):
    # 인덱스 a: 0부터 n - 1까지 반복하면서
    for a in range(1, n + 1):
        # 인덱스 b: 0부터 n- 1까지 반복하면서
        for b in range(1, n + 1): 
            # distance[a][b] 는 distance[a][b], distance[a][k] + distance[k][b] 중 작은것으로 초기화 
            distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

# 인덱스 i: 0부터 n - 1까지 반복하면서
for i in range(1, n + 1): 
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(1, n + 1):
        # distance[i][j]가 INF보다 같거나 크면
        if distance[i][j] >= INF: 
            # 0출력 (end는 스페이스로)
            print(0, end = ' ')
        # 나머지경우 
        else: 
            # distance[i][j] 출력 (end는 스페이스로)
            print(distance[i][j], end = ' ')
    # 한줄띄우기
    print()
