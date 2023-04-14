def solution(food):
    answer = ''
    rev = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    rev = answer[::-1]
    answer += '0' 
    
    return answer + rev