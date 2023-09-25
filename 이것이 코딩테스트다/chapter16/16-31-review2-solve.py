"""
n * m 크기 금광. 1 * 1 크기 칸으로 나뉨
첫번째 열부터 출발하여 금 캐시 시작
첫번째 열 어느행에서든 출발 가능
m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지중 하나위치로 이동
채굴자가 얻을 수 있는 금 최대 크기 출력

현재 행, 열에서 얻을 수있는 최대 크기는 
    이전 행, 이전 열 금 최대에서 현재꺼, 
    현재 행, 이전 열 최대 금에서 현재꺼, 
    다음 행, 이전 열 최대 금에서 현재꺼 
    중 가장 큰 것 
0번째 행이면 이전 행이 없음
마지막 행이면 다음행이 없음 
"""

# 테스트케이스 t 입력
t = int(input()) 
# t번만큼 반복하면서
for _ in range(t): 
    # n, m 공백 구분으로 입력 
    n, m = map(int, input().split()) 
    # golds n * m 크기로 입력 
    golds = [[0] * m for _ in range(n)]
    # 매장된 금 개수 입력 data
    data = list(map(int, input().split()))
        
    for i in range(n):
        for j in range(m):
            golds[i][j] = data[i * m + j] 
    
    # dp n * m 크기의 2차원 리스트 
    dp = [[0] * m for _ in range(n)]
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n):
        # dp[i][0] = golds[i][0]
        dp[i][0] = golds[i][0] 
        
    # 인덱스 j: 1부터 m - 1까지 반복하면서
    for j in range(1, m): 
        # 인덱스 i: 0부터 n - 1까지 반복하면서 
        for i in range(n):
            # 이전 행, 이전 열 g1 : i가 0이면 0, 0이 아니면 dp[i - 1][j - 1]
            g1 = 0 if i == 0 else dp[i - 1][j -1]
            # 현재 행, 이전 열 g2 : dp[i][j - 1]
            g2 = dp[i][j - 1]
            # 다음 행, 이전 열 g3 : i갸 n - 1이면 0, 0이 아니면 dp[i + 1][j- 1]
            g3 = 0 if i == n - 1 else dp[i + 1][j - 1]
            # dp[i][j] 는 g1, g2, g3중 큰 거 + golds[i][j] 
            dp[i][j]  = max(g1, g2, g3) + golds[i][j] 
    
    # 현재 최대 크기 max_gold는 dp[0][m - 1]
    max_gold = dp[0][m - 1]
    # 인덱스 i: 1부터 n - 1까지 반복하면서
    for i in range(1, n):
        # max_gold는 max_gold와 dp[i][m - 1]중 큰거 
        max_gold = max(max_gold, dp[i][m - 1])
    
    # max_gold 출력 
    print(max_gold)