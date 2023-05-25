def solution(s):
    answer = 0
    
    x_count = 0
    other_count = 0
    
    for i in s:
        if x_count == other_count:
            answer += 1
            a = i
        if i == a:
            x_count += 1
        else:
            other_count += 1
    
    return answer