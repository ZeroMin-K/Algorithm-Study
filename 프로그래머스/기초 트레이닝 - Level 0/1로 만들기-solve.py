def solution(num_list):
    answer = 0
    for num in num_list:
        count = 0 
        while num != 1: 
            if num % 2: 
                num = (num - 1) // 2
            else:
                num //= 2
            count += 1
        answer += count 
    
    return answer