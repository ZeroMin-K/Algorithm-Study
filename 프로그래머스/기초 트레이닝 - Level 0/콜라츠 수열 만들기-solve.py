def solution(n):
    answer = [n]
    while answer[-1] != 1:
        num = 3 * answer[-1] + 1
        if answer[-1] % 2 == 0:
            num = answer[-1] // 2
        answer.append(num) 
    return answer