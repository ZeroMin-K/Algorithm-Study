from collections import deque 

def solution(s):
    answer = 0
    
    q = deque(s)
    while q:
        a, b = 1, 0
        x = q.popleft()
        
        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1
                
            if a == b:
                answer += 1
                break
                
    if a != b:
        answer += 1
    
    return answer