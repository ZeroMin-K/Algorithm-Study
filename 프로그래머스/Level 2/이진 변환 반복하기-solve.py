"""
0과1로 이루어진 문자열 x 이진 변환
1. x의 모든 0제거 
2. x의길이 c. x를 c를 2진법으로 표현한 문자열로 바꿈
s가 "1"이 될때까지 이진변환을 했을때 변환 횟수, 제거된 모든 0의 개수를 배열에 담아 return 

s가 "1"이 될때까지 반복하면서 
0의 개수를 세고, 0 제거했을때 만들어진 문자열의 길이를 2진법으로 만들고 변환횟수 증가 
"""

def solution(s):
    # 변환 횟수 converted 0으로 초기화 
    converted = 0
    # 제거된 0의 개수 zeros 0으로 초기화 
    zeros = 0
    
    # s가 "1"이 아닌동안 반복 진행
    while s != "1":
        # s에서 0의 개수를 세고 zeros에 더함
        zeros += s.count("0")
        # s에서 "0"을 ""로 변경
        s = s.replace("0", "")
        # s의 길이를 2진수로 변경후 s에 저장 
        s = bin(len(s))[2:]
        # converted 1 증가 
        converted += 1
    
    return [converted, zeros]