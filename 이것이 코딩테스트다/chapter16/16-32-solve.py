"""
현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것중만 선택해서 
아래층으로 내려올때 합이 최대가 되는 경로 구하기 
"""

# 삼각형의 크기 n 입력
n = int(input())

# 삼각형 리스트 tri 생성 
tri = []
# n번 반복하며 
for _ in range(n):
    # 공백 기준 정수들 입력 
    tri.append(list(map(int, input().split())))

# 왼쪽에서 왔을때와 오른쪽에서 왔을때 합이 가장 큰거 선택하는 DP
# 왼쪽 모서리 => 왼쪽에서 오는게 없음 (j = 0 일 때)
# 오른쪽 모서리 => 오른쪽에서 오는게 없음 (i = j 일 때)

# 현재 위치 [i][j], 왼쪽 모서리 [i-1][j-1], 오른쪽 모서리 [i-1][j]
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
# 왼쪽 모서리 => dp[i][j] = dp[i-1][j] + tri[i][j]
# 오른쪽 모서리 => dp[i][j] = do[i-1][j-1] + tri[i][j]

# 인덱스 i  1부터 크기n의 n-1까지 반복하면서
for i in range(1, n):
    for j in range(len(tri[i])):
        # 왼쪽 모서리 이면
        if j == 0:
            tri[i][j] = tri[i-1][j] + tri[i][j]
        # 오른쪽 모서리 이면
        elif i == j:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        # 나머지의 경우 
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]

# 삼각형의 n-1행에서 최대 치 출력 
print(max(tri[n-1]))