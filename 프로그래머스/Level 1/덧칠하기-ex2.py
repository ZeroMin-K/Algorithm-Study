from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    
    while section:
        start = section.popleft()
        
        while section:
            if section[0] >= start + m:
                break
            section.popleft()
            
        answer += 1
        
    return answer