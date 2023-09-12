"""
자연수 x를 y로 변환
사용가능한 연산
- x에 n을 더함
- x에 2를 곱함
- x에 3을 곱함
x, y, n: 자연수 
return : x를 y로 변환하기 위해 필요한 최소연산 횟수 
    - 만들수없다면 -1 출력 
"""
def solution(x, y, n):
    # 최소 연산 횟수를 찾기 위해 연산횟수 최대 값 INF 정수 1e9로 초기화 
    INF = int(1e9)
    # 인덱스까지 최소 연산 횟수에 대한 dp 테이블 : 값은 INF, y + 1 길이의 리스트로 생성 
    dp = [INF] * (y + 1)
    # dp[x]는 0으로 초기화 
    dp[x] = 0 
    # 사용할 수 있는 연산 리스트 operators
    operators = [(1, n), (2, 0), (3, 0)]
    # 인덱스 k : x부터 y까지 반복하면서 
    for k in range(x, y + 1): 
        # operators를 하나씩 탐색하면서 : 원소 operator
        for operator in operators: 
            # k에서 operators 연산을 하게되는 다음 인덱스 next의 값은 k * oprator[0] + operator[1]
            next = k * operator[0] + operator[1] 
            # next가 y보다 같거나 작으면
            if next <= y: 
                # dp[next]의 값은 dp[next], dp[k] + 1 중 작은 값
                dp[next] = min(dp[next], dp[k] + 1) 
    
    # dp[y]가 INF이면 -1 아니면 dp[y]가 리턴 
    return dp[y] if dp[y] != INF else -1