"""
n * m 크기 미로방  - 가장 왼쪽 윗방 (1, 1), 가장 오른쪽 방 (n, m )
(1, 1) 에서 (n, m)으로 이동 
(r, c)에 있을 때 (r + 1, c), (r, c + 1), (r + 1, c + 1)로 이동 (하, 우, 하우)
방문하면서 사탕 모두 가져감 
(n, m)로 이동할때 가져올 수 있는 사탕 개수의 최댓값 

현재 위치 (r, c)에서 사탕 최대 개수는 (r+ 1, c) , (r, c + 1), (r + 1, c + 1) 중 가장 큰 개수에서 
현재 위치의 큰 개수를 더한 것 
"""

import sys
input = sys.stdin.readline

# 미로크기 n, m 입력
n, m = map(int, input().split())

miro = []

# n번 반복하면서 
for _ in range(n):
    # m개의 숫자 입력 
    candies = list(map(int, input().split()))
    miro.append(candies) 

dp = [[0] * m for _ in range(n)]
dp[0][0] = miro[0][0]

moves = [(-1, -1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(m):
        befores = [0]
        for move in moves:
            before_x = i + move[0]
            before_y = j + move[1]

            if 0 <= before_x < n and 0 <= before_y < m:
                befores.append(dp[before_x][before_y])
        
        dp[i][j] = max(befores) + miro[i][j]

print(dp[n - 1][m - 1])