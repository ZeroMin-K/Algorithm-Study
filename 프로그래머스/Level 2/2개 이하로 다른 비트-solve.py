"""
양의 정수 x
f(x) : x보다 크고 x와 비트가 1 ~ 2 개 다른 수들 중에서 제일 작은 수 
numbers: 정수들이 담긴배열
return : numbers의 모든 수들에 대하여 각 수의 f값을 담은 배열 
"""
def solution(numbers):
    answer = []
    for number in numbers: 
        fx = number + 1
        if number % 2:
            number = '0' + bin(number)[2:]
            number_idx = number.rfind('01')
            fx = int(number[:number_idx] + '10' + number[number_idx + 2:], 2)
        answer.append(fx)
            
    return answer