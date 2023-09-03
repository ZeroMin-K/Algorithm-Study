"""
n명의 병사 무작위 나열
병사배치할때 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야함
특정 위치 병사를 열외하여 남아있는 병사 수 최대로
열외하는 병사수 출력
"""
n = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1) 

print(n - max(dp))