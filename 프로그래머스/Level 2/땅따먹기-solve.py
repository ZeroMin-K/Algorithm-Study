"""
땅따먹기 게임 땅 land : n행 4열. 모든 칸에 점수 있음
1행부터 땅을 밟으며 한행씩 내려올때 각행 4칸 중 한칸만 밟으면서 내려옴
한 행씩 내려올때 같은 열을 연속해서 밟을 수 없음
return : 마지막행까지 모두 내려왔을때 얻을 수 있는 점수의 최댓값

점수의 최대값은 마지막 행 1열, 2열, 3열, 4열 중에서 최댓값
마지막 행의 1열은 이전 행 2열, 3열, 4열 중 최댓값 + 마지막 행 1열 값
마지막 행의 2열은 이전 행 1열, 3열, 4열 중 최댓값 + 마지막 행 2열 값 
...
현재 행, 현재 열의 최댓값은 이전 행, 현재 열을 제외한 나머지 열의 최댓값 + 현재행, 현재 열 값 
=> DP 

현재 행 i, 현재 열 j의 최댓값 dp[i][j]. a,b,c는 1~4열 중 j가 아닌 열
dp[i][j] = max(dp[i - 1][a], dp[i - 1][b], dp[i - 1][c]) + land[i][j] 
"""

def solution(land):
    answer = 0
    # land 행의 길이 n 
    n = len(land) 
    # land 열의 길이 cols
    cols = len(land[0])
    
    # dp 테이블 n * cols 길이의 2차원 리스트로 초기화
    dp = [[0] * cols for _ in range(n)]
    
    # << 0행일 때 dp 테이블 값 초기화 >>
    # 인덱스 j: 0부터 cols - 1까지 반복하면서 
    for j in range(cols): 
        # dp[0][j] = land[0][j] 
        dp[0][j] = land[0][j] 
    
    # << dp 진행 >>
    # 인덱스 i: 1부터 n - 1까지 반복하면서 (행) 
    for i in range(1, n): 
        # 인덱스 j: 0부터 cols - 1까지 반복하면서 (열) 
        for j in range(cols): 
            # 이전 행의 최댓값들을 담는 리스트 before 빈리스트로 초기화 
            before = [] 
            # 인덱스 k: 0부터 cols - 1까지 반복하면서 
            for k in range(cols): 
                # j와 k가 다르면 
                if j != k: 
                    # before에 dp[i - 1][k] 삽입 
                    before.append(dp[i - 1][k])
            # dp[i][j] 값은 before 중 큰 값 + land[i][j] 
            dp[i][j] = max(before) + land[i][j] 
    

    # dp[n - 1]에서 큰 값 출력 
    return max(dp[n - 1])