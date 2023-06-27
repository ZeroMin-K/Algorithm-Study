def solution(n):
    answer = 0
    for x in range(1, n + 1):
        part_sum = 0
        for y in range(x, n + 1):
            part_sum += y
            if part_sum == n:
                answer += 1
                break
            elif part_sum > n:
                break
    
    return answer