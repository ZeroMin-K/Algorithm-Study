def solution(left, right):
    answer = []
    for num in range(left, right + 1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count % 2 == 0:
            answer.append(num)
        else:
            answer.append(-1 * num)
    
    return sum(answer)