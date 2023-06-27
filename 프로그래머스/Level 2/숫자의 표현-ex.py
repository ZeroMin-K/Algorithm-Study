def solution(n):
    answer = 0
    for i in range(1, n + 1):
        part_sum = 0
        while part_sum < n:
            part_sum += i
            i += 1
        if part_sum == n:
            answer += 1
    
    return answer