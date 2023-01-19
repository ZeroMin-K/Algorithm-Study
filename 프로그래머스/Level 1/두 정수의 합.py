def solution(a, b):
    x = max(a, b)
    y = min(a, b)
    
    return (x + 1) * x / 2 - (y + 1) * y / 2 + y