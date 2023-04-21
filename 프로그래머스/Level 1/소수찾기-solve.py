import math 

def solution(n):
    # (n + 1) 까지 소수 판별인지 여부에 대한 리스트(True로 초기화)
    primes = [True] * (n + 1)
    # 1은 소수가 아니므로 False
    primes[1] = False 
    
    # 인덱스 i - 2부터 숫자 n의 제곱근까지 반복하면서
    for i in range(2, int(math.sqrt(n)) + 1):
        # 곱할 수 k = 2
        k = 2
        # i * k 가 n보다 작을때까지 반복하면서
        while i * k <= n: 
            # i * k 는 False (소수가 아님)
            primes[i * k] = False
            # k에 1증가 
            k += 1
            
    # 소수의 개수는 0 
    total = 0
    # 인덱스 i - 2부터 숫자 n 까지 반복하면서
    for i in range(2, n + 1): 
        # 소수리스트 i가 True이면
        if primes[i]: 
            # 소수 개수 증가 
            total += 1
        
    return total