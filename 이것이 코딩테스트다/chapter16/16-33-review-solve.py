"""
N + 1일째 되는날 퇴사하기 위해 남은 N일 동안 많은 상담 진행
상담완료하는데 걸리는 시간 Ti
상담했을 때 받을 수 있는 금액Pi
최대 수익 구하는 프로그램 

"""

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
dp = [0] * (n + 2) 

print(days)
print(prices)
print(dp)

# 인덱스 i:
for i in range(1, n + 1): 

    print('----')
    print('현재 날짜: ', i )

    # next_day는 i + days[i] 
    next_day = i + days[i]

    print('다음날짜: ', next_day)

    # next_day 가 n보다 작으면
    if next_day <= n + 1: 

        print('오늘 상담하면 : ', dp[i] + prices[i])
        print('다음 날짜 원래 이익: ', dp[next_day])
        print('어제까지 이익: ', dp[next_day - 1])


        # dp[next_day]는 dp[i] + prices[i], dp[next_day - 1]중 큰값
        dp[next_day] = max(dp[i] + prices[i], dp[next_day], dp[next_day - 1])

        print('>>최종: ', next_day, '날 이익: ', dp[next_day])
        
# dp[n ] 출력
print(max(dp))