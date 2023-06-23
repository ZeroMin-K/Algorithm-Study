"""
어떤 문자열에 대해 접두사는 특정 인덱스까지 문자열 의미 

is_prefix길이만큼 반복하면서 is_prefix 문자와 my_string문자가 같은지 확인 
is_prefix길이가 더 길면 접두사가 아님
"""

def solution(my_string, is_prefix):
    answer = 1
    
    if len(is_prefix) > len(my_string):
        return 0  
    
    for i in range(len(is_prefix)):
        if my_string[i] != is_prefix[i]:
            answer = 0 
            
    return answer