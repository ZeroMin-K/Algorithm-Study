"""
x가 5로 나누어떨어지면 5로 나눔
x가 3으로 나누어떨어지면 3으로 나눔
x가 2로 나누어떨어지면 2로 나눔
x에서 1뺌

연산 4개를 사용해서 1로 만듬
연산을 사용하는 횟수의 최솟값 출력 
dp[i] - 현재 인덱스 i 수에서 연산 사용한 최소 횟수
do[i] = min(dp[x * 5], dp[x * 3], dp[x* 2], dp[x + 1]) + 1

"""

x = int(input())
dp = [0] * (x+1)

for i in range(x - 1, 0, -1):
    dp[i] = dp[i + 1] + 1

    if i * 5 <= x:
        dp[i] = min(dp[i * 5] + 1, dp[i]) 
    
    if i * 3 <= x:
        dp[i] = min(dp[i * 3] + 1 , dp[i])
    
    if i * 2 <= x:
        dp[i] = min(dp[i * 2] + 1, dp[i]) 
    
print(dp[1])