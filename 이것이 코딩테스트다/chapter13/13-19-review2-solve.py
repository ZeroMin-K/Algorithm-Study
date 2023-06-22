"""
n개의 수로 이루어진 수열. 
수와 수 사이에 끼워넣을 수 있는 n - 1개 연산자.
    - 덧셈, 뺄셈, 곱셈, 나눗셈으로 이루어짐
수와 수 사이에 연산자를 하나씩 넣어 수식 만듬
수의 순서 못바꿈. 연산자 우선순위 무시하고 앞에서부터 계산 진행
만들 수 있는 식의 결과가 최대인 것과 최소인것 구하기 
"""

# 수의 개수 n 입력
n = int(input())
# 공백으로 구분된 수열을 int로 map 후 리스트 nums로 입력
nums = list(map(int, input().split()))
# 덧셈 개수 add, 뺄셈 개수 sub, 곱셈 개수 mul, 나눗셈개수 div 입력후 int로 map함
add, sub, mul, div = map(int, input().split())

# 최대값 max_result 0으로 초기화
max_result = -int(1e9)
# 최솟값 min_result int(1e9)로 초기화
min_result = int(1e9) 

# DFS 함수 선언 
# - 매개변수 현재 계산해야할 수의 인덱스 k, 
#          - 현재 결과 result 
#          - 덧셈 개수 add, 뺄셈개수 sub, 곱셈개수 mul, 나눗셈개수 div
def dfs(k, result, add, sub, mul, div): 
    # max_result, min_result global로 선언
    global max_result, min_result 
    # k가 n과 같으면
    if k == n - 1: 
        # max_result와 result중 큰 값 비교
        max_result = max(max_result, result) 
        # min_result와 result 중 작은 값 비교
        min_result = min(min_result, result)
        # 리턴
        return 
        
    # add개수가 0보다 크면
    if add > 0: 
        # dfs호출 인자 k + 1, result + nums[k], add -1, sub, mul, div 
        dfs(k + 1, result + nums[k + 1], add - 1, sub, mul, div)
        
    # sub개수가 0보다 크면
    if sub > 0:
        # dfs호출 - 인자 k + 1, result - nums[k], add, sub - 1, mul, div
        dfs(k + 1, result - nums[k + 1], add, sub - 1, mul, div) 
        
    # mul개수가 0보다 크면
    if mul > 0: 
        # dfs 호출 - 인자 k + 1, result * nums[k], add, sub, mul - 1, div
        dfs(k + 1, result * nums[k + 1], add, sub, mul - 1, div)
        
    # div개수가 0보다 크면
    if div > 0: 
        # dfs호출 - 인자 k + 1, int(result / nums[k]), add, sub, mul, div - 1
        dfs(k + 1, int(result / nums[k + 1]), add, sub, mul, div - 1)
        

# dfs 호출 - 인자 0, nums[0], add, sub, mul, div
dfs(0, nums[0], add, sub, mul, div) 
# max_result 출력
print(max_result)
# nin_result 출력
print(min_result)