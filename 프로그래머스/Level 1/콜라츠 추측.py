def solution(num):
    # 몇번 하는지 수 세는 count
    count = 0
    
    # num이 1이면 
    if num == 1:
        # 0 리턴
        return 0
    
    while count < 500:
        # 짝수이면 
        if num % 2 == 0:
            # 2로 나눔
            num //= 2
        # 홀수이면
        else:
            # 3을 곱하고 1을 더함 
            num = num * 3 + 1
            
        # count 증가
        count += 1
        # 1이 될때까지 반복 
        if num == 1:
            return count
        
    # count가 500번이 넘기면 -1 리턴 
    return -1