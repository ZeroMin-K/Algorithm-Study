# n 입력 
n = int(input()) 
# 각 걸리는 시간에 대한 리스트 days  초기화
days = [0]  * (n + 1) 
# 해당 날짜 상담 진행히 얻는 이익 prices 초기화 
prices = [0] * (n + 1) 
# n번 반복하면서
for i in range(n): 
    # t, p 입력 
    t, p = map(int, input().split())
    days[i + 1] = t 
    prices[i + 1] = p 

# dp 초기화 값은 0 길이는 n
dp = [0] * (n + 1) 

# 인덱스 i:
for i in range(1, n + 1): 
    dp[i] = max(dp[i], dp[i - 1])

    # next_day는 i + days[i] 
    next_day = i + days[i] - 1

    # next_day 가 n보다 작으면
    if next_day <= n: 
        # dp[next_day]는 dp[i] + prices[i], dp[next_day - 1]중 큰값
        dp[next_day] = max(dp[i - 1] + prices[i], dp[next_day])

# dp[n ] 출력
print(max(dp))
