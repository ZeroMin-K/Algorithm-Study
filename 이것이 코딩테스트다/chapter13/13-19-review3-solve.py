"""
n개의 수로 이루어진 수열 a1, a2..an
수와 수 사이에 끼워넣을 수 있는 n - 1개 연산자 : +, -, x, /로만 이루어짐
수와 수사이에 연산자르 ㄹ하나씩 넣어 수식을 만듬
수의 순서를 바꾸면 안됨 
연산자 우선순위 무시, 앞에서부터 진행. 나눗셈은  정수 나눗셈 몫만 취함

n개의 수 , n - 1개 연산자가 주어졌을 때 만들 수 있는 식의 결과가 최대인것과 최소인것 구하기 
"""

# 수의 개수 n 입력
n = int(input()) 
# 수열 a1, ..an 리스트로 입력 seq
seq = list(map(int, input().split()))
# 덧셈의 개수 add, 뺄셈게수 sub, 곱셈 개수 mul, 나눗셈 개수 div 입력 
add, sub, mul, div = map(int, input().split()) 

# 최댓값 max_result -1e9로 초기화
max_result = -int(1e9) 
# 최솟값 min_result 1e9로 초기화
min_result = int(1e9) 

# 백트래킹 dfs 함수 선언 : 매개변수 depth, 현재 결과 result, 연산 개수 add, sub, mul, div 
def dfs(depth, result, add, sub, mul, div):
    # max_result, min_result global로 선언
    global max_result, min_result

    # depth가 seq의 길이와 같으면
    if depth == len(seq): 
        # max_result는 max_result와 result중 큰값
        max_result = max(max_result, result) 
        # min_result는 min_result와 result중 작은 값
        min_result = min(min_result, result) 
        # 리턴 
        return 

    # add가 0보다 크면
    if add > 0: 
        # dfs 호출 : depth + 1, result + seq[depth], add - 1, sub, mul, div
        dfs(depth + 1, result + seq[depth], add - 1, sub, mul, div)
    # sub가 0보다 크면
    if sub > 0: 
        # dfs 호출 : depth + 1, result - seq[depth], add, sub - 1, mul, div
        dfs(depth + 1, result - seq[depth], add, sub - 1, mul, div)
    # mul가 0보다 크면
    if mul > 0: 
        # dfs 호출 : depth + 1, result * seq[depth], add, sub, mul - 1, div
        dfs(depth + 1, result * seq[depth], add, sub, mul - 1, div)
    # div가 0보다 크면
    if div > 0: 
        # dfs 호출: depth + 1, result // seq[depth], add, sub, mul, div - 1
        dfs(depth + 1, int(result / seq[depth]), add, sub, mul, div - 1)

# dfs 호출: 0, 0, add, sub, mul, div 
dfs(1, seq[0], add, sub, mul, div)

# max_result 출력
print(max_result) 
# min_result 출력
print(min_result)