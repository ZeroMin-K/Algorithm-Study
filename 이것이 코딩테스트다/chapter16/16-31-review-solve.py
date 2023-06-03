"""
n * m 크기 금광. 1 * 1 크기 칸으로 나뉨. 특정한 크기 금있음
첫번째 열부터 출발하여 금 캐기 시작
첫번째 열 어느행이든 출발가능
m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나 위치로 이동
얻을 수 있는 최대 크기출력

DP를 이용한 풀이 
현재 위치에서 최대값은 왼쪽 대각선 위, 왼쪽, 왼쪽대각선 아래에서 온 금들 중 큰값을 더함

0 1 2 3 4 5 6 7
n * m : 2 * 4
0번째 행: 0(0, 0) 1(0, 1) 2(0, 2) 3(0, 3) 
1번째 행: 4(1, 0) 5(1, 1) 6(1, 2) 7(1, 3) 
i // m , i % m 

"""

# 테스트케이스 t입력
t = int(input())
# t번 반복하면서 
for _ in range(t):
    # n, m 공백 구분하여 입력
    n, m = map(int, input().split())
    # n * m 개 위치 금의 개수가 공백으로 구분되어 입력
    data = list(map(int, input().split()))
    
    golds = [[0] * m for _ in range(n)]
    for i in range(len(data)):
        golds[i // m][i % m] = data[i]
    
    # 왼쪽위에서, 왼쪽, 왼쪽 아래에서 오는 경우에 대한 이동 리스트
    dx = [-1, 0, 1]
    dy = [-1, -1, -1]
    
    # 인덱스 j: 1부터  m - 1까지 반복하면서 (열 이동)
    for j in range(1, m):
        # 인덱스 i: 0부터 n - 1까지 반복하면서 (행 이동)
        for i in range(n):
            # 이전에서 오는 값들을 담는 리스트 befores
            befores = [] 
            # 인덱스 k: 0부터 2까지 반복하면서
            for k in range(3):
                # 이전 x좌표 i + dx[k]
                x = i + dx[k]
                # 이전 y좌표 j + dy[k]
                y = j + dy[k]
                # x가 0보다 같거나 크고, n보다 작고, y가 0보다 같거나 크고 m보다 작으면
                if 0 <= x < n and 0 <= y < m:
                    # befores에 dp[x][y]를 append
                    befores.append(golds[x][y])
            if len(befores) > 0:
                # 현재 dp[i][j]의 값은 현재 위치의 값 + befores에서 최댓값 
                golds[i][j] += max(befores) 
            
    # 금의 최대 크기 = 0
    max_gold = 0
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n):
        # 금의 최대 크기와 [i][m-1]중 가장 큰것을 저장
        max_gold = max(max_gold, golds[i][m - 1])
    # 금의 최대 크기 출력 
    print(max_gold)