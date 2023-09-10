"""
numbers: 정수로 이뤄진 배열
배열의 각원소들에 대해 자신보다 뒤에 있는 숫자중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수
return : 모든 원소에 대한 뒷 큰수들을 차례대로 담은 배열
    - 뒷큰수 존재하지 않는 원소는 -1 담음 
"""

def solution(numbers):
    big_nums = [0] * len(numbers)
    stack = [] 
    stack.append((0, numbers[0]))
    
    for i in range(1, len(numbers)):
        while stack and stack[-1][1] < numbers[i]:
            idx, num = stack.pop()
            big_nums[idx] = numbers[i]
        stack.append((i, numbers[i]))
    
    while stack:
        idx, num = stack.pop()
        big_nums[idx] = -1
    
    return big_nums