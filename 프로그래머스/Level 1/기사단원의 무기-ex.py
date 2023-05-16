def solution(number, limit, power):
    
    divisor_nums = []
    
    for j in range(1, number + 1):
        cnt = 0
        for i in range(1, int(j ** 0.5) + 1):
            if j == i ** 2:
                cnt += 1
            elif j % i == 0:
                cnt += 2
        divisor_nums.append(cnt)
        
    result = [i if i <= limit else power for i in divisor_nums]
    return sum(result)