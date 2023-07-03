def solution(n):
    fibos = [0] * 100001
    fibos[1] = 1
    fibos[2] = 1
    
    for i in range(2, n + 1):
        fibos[i] = fibos[i - 1] + fibos[i - 2]
        
    return fibos[n] % 1234567