"""
N + 1일째 되는 날 퇴사를 하기위해 남은 N일 동안 최대한 많은 상담 진행
상담을 완료하는데 걸리는 기간 Ti, 상담을 했을때 받을 수 있는 금액 Pi
상담을 적절히했을때 최대 수익 출력 

1일에서 1일만 상담하면 1 + 1 => 1일차일때 상담 완료 2일차부터 상담시작 
1일에서 2일동안 상담하면 1 + 2  => 2일차일때 상담 완료 3일차부터 상담 시작 
현재 날짜의 상담을 선택한다고 하면 현재 상담하게되면 완료되는 다음날에서 최대값을 비교 

"""

# n 입력
n = int(input())
# 상담시 걸리는 시간을 담는 리스트 times- 값을 0으로 길이는 n + 1로 초기화
times = [0] * (n + 1) 
# 상담시 받을 수 있는 금액을 담는 리스트 prices - 값을 0으로 길이는 n + 1로 초기화 
prices = [0] * (n + 1)
# 인덱스 i: 1부터 n까지 반복하면서 
for i in range(1, n + 1):
    # 시간 time, 금액 price 공백 구분으로 입력 (1일부터 N일까지) 
    time, price = map(int, input().split())
    # 인덱스 i 날짜 상담의 걸리는 시간 times의 값은 time
    times[i] = time
    # 인덱스 i 날짜 상담의 금액 prices의 값은 price
    prices[i] = price 

# 최대 수익 dp 테이블 dp - 값을 0으로 길이 n + 1로 초기화 
dp = [0] * (n + 2) 
# 인덱스 i: 1부터 n까지 반복하면서 
for i in range(1, n + 1): 
    # i번째 날짜를 선택시 i번째 완료하는 날의 다음날 최댓값은 i번째 완료하는 날 값과 i번째 날 최댓값 + i날 상담 금액 
    next_day = i + times[i] 
    if next_day <= n + 1:

        print('-----------')
        print('현재 날짜: ', i)
        print('완료 날짜: ', next_day)
        print('완료 날짜 원래 돈: ', dp[next_day])
        print('현재 날짜 상담 선택시 그때 돈: ', dp[i] + prices[i])
    
        dp[next_day] = max(dp[next_day], dp[i] + prices[i], dp[next_day - 1])

        print('다음날짜 최종 돈: ', dp[next_day])

print(dp)
# 최대 수익테이블에서 최대값 출력
print(max(dp))