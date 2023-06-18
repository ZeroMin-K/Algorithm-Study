def solution(arr):
    answer = []
    for num in arr:
        elem = num 
        if num >= 50 and num % 2 == 0:
            elem = num // 2
        elif num < 50 and num % 2 == 1:
            elem = num * 2
        
        answer.append(elem)
        
    return answer