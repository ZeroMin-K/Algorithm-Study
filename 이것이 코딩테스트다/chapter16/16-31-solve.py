"""
n * m 크기의 금광 
첫번째 열부터 출발하여 금을 캐기 시작 - 첫번째 열의 어느행에서든 출발
m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지중 하나의 위치로 이동
금의 최대 크기 출력 

DP를 이용하여 풀이하기 
"""

# 테스트케이스 T 입력
t = int(input())
# 테스트케이스 T만큼 반복
for _ in range(t):
    # n, m 공백으로 구분되어 입력 
    n, m = map(int, input().split())
    
    # n * m 개위치에 매장된 금의 개수 공백으로 구분되어 입력 
    data = list(map(int, input().split()))
    
    golds = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            golds[i][j] = data[i * m + j]
    
    # n, m 에 맞는 dp 테이블 생성
    dp = [[0] * m for _ in range(n)]
    
    # 각 0번째 열에 대해 dp 테이블 값 초기화
    for i in range(n):
        dp[i][0] = golds[i][0]
    
    # 이전위치에서 현재 위치까지 오기위한 움직임 리스트 (-1, -1), (0, -1), (1, -1)
    moves = [(-1, -1), (0, -1), (1, -1)]
    
    # 인덱스 j  - 열 1부터 m - 1까지 반복하면서
    for j in range(1, m):
        # 인덱스 i - 행 0 부터 n - 1까지 반복하면서
        for i in range(n):
            # 이전 좌표에 있는 값들 저장하는 임시리스트 
            temp = [] 
            # 움직임 리스트하나씩 반복하면서
            for move in moves: 
                # 이전 좌표는 움직임 리스트에 더한것
                before_i = i + move[0]
                before_j = j + move[1]
                # 이전 좌표가 n * m 위치에 있으면
                if 0 <= before_i < n and 0 <= before_j < m:
                    # 이전 좌표에 있는 값들 저장하는 임시 리스트에 dp[이전좌표]append
                    temp.append(dp[before_i][before_j])
                    
            # dp[i][j] = 이전좌표리스트 최대값 + 현재 [i][j]값 
            dp[i][j] = max(temp) + golds[i][j]
    
    # 금의 최대 크기 출력 m -1 열에서 가장 큰 값 찾기 
    print(max([dp[i][m-1] for i in range(n)]))