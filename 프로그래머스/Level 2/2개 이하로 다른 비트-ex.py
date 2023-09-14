def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(((number ^ (number + 1)) >> 2) + number + 1)
    
    return answer