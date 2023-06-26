def solution(s):
    # 변환 횟수 converted 0으로 초기화 
    converted = 0
    # 제거된 0의 개수 zeros 0으로 초기화 
    zeros = 0
    
    # s가 "1"이 아닌동안 반복 진행
    while s != "1":
        ones = s.count("1")
        zeros += len(s) - ones 
        s = bin(ones)[2:]
        converted += 1
    
    return [converted, zeros]