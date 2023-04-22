"""
n마리 폰켓몬 중에서 n /2 마리 가져가도 됨
최대한 많은 종류의 폰켓몬 선택

set를 이용하여 각 종류를 셈
n/2가 종류보다 많거나 크면 최대 종류는 결국 그종류 

"""

def solution(nums):
    total_unique_type = len(list(set(nums)))
    
    if len(nums) // 2 >= total_unique_type:
        return total_unique_type
    
    return len(nums) // 2