"""
n개의 음이 아닌 정수들
정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟넘버 만들기
numbers: 사용할 수 있는 숫자가 담긴 배열
target: 타겟 넘버 
return : 숫자를 적절히 더하고 빼서 타겟 넘버만드는 방법의 수 
백트래킹을 이용하여 타겟넘버가 되는 경우의 수 세기 
"""
# dfs 함수 선언 
# - 매개변수 현재 깊이 (numbers에서 인덱스) depth, 숫자 리스트 numbers,
# -         현재까지 결과 result, 타겟넘버 target
def dfs(depth, numbers, result, target):
    global answer 
    # depth가 len(numbers) 이고 result가 target과 같으면 
    if depth == len(numbers) and result == target:
        # answer 1 증가 
        answer += 1
        # 리턴 
        return 
    
    # depth가 len(numbers)보다 크면
    if depth >= len(numbers):
        # 리턴
        return 
    
    # dfs 호출 - 인자 depth + 1, numbers, result + numbers[depth], target)
    dfs(depth + 1, numbers, result + numbers[depth], target)
    # dfs 호출 - 인자 depth + 1, numbers, result - numbers[depth], target)
    dfs(depth + 1, numbers, result - numbers[depth], target)

def solution(numbers, target):
    global answer 
    # answer을 0으로 초기화 
    answer = 0
    
    # dfs호출 - 인자 0, numbers, 0, target
    dfs(0, numbers, 0, target)
    
    return answer