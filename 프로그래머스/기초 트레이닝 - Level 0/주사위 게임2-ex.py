def solution(a, b, c):
    diff_nums = len(set([a, b, c]))
    answer = a + b + c
    
    if diff_nums == 2:
        answer *= a ** 2 + b ** 2 + c ** 2
    elif diff_nums == 1:
        answer *= (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
        
    return answer