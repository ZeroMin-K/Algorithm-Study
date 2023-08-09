def cal_score(n, a, b, c):
    return a ** n + b ** n + c ** n

def solution(a, b, c):
    answer = cal_score(1, a, b, c)
    
    if (a == b and b != c) or (b == c and a != b) or (c == a and a != b):
        answer *= cal_score(2, a, b, c)
    elif a == b and b == c: 
        answer *= cal_score(2, a, b, c) * cal_score(3, a, b, c)
        
    return answer