"""
arr(x) = arr(x + 1) => 이전과 작업 이후가 같다 
50보다 크거나 같은 짝수이거나 50보다 작은 홀수이면 원소 변경
=> 50보다 큰 홀수 이거나 50보다 작은 짝수이면 원소 변경하지 않음

각 원소들에 대해 50보다 큰 홀수가 될때까지, 50보다 작은 짝수가 될때까지 작업을 몇번반복하는지 확인
"""

def check(result):
    if (result > 50 and result % 2 == 1) or \
        (result < 50 and result % 2 == 0):
        return False
    return True 

def solution(arr):
    answer = 0
    for num in arr:
        result = num 
        rep = 0
        while check(result):
            if result >= 50 and result % 2 == 0: 
                result //= 2
            elif result < 50 and result % 2 == 1:
                result = result * 2 + 1
            
            rep += 1
            
        answer = max(answer, rep) 

    return answer