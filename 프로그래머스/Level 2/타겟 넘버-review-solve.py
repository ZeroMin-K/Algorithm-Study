"""
n개의 음이 아닌 정수들
순서를 바꾸지 않고 적절히 더하거나 빼서 타겟넘버 만들기 
numbers: 숫자 담긴 배열
target: 타겟넘버
return : 타겟 넘버 만드는 방법 수 
"""
def dfs(depth, numbers, result, target):
    global answer 
    if depth == len(numbers):
        if result == target:
            answer += 1
        return
    
    dfs(depth + 1, numbers, result + numbers[depth], target)
    dfs(depth + 1, numbers, result - numbers[depth], target)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, 0, target)
    return answer