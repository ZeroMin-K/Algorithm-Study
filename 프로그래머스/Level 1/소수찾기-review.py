import math 

def solution(n):
    answer = 0
    primes = [True] * (n + 1) 
    primes[1] = False
    
    
    for i in range(2, int(math.sqrt(n)) + 1):
        k = 2
        while i * k <= n:
            primes[i * k] = False
            k += 1
    
    for i in range(1, n + 1):
        if primes[i]:
            answer += 1
        
    return answer