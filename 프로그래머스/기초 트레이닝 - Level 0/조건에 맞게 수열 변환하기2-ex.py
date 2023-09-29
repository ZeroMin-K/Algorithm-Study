def solution(arr):
    answer = 0
    before = arr
    
    while True:
        after = []
        
        for num in before:
            if num >= 50 and num % 2 == 0:
                num //= 2
            elif num < 50 and num % 2 == 1:
                num = num * 2 + 1
            after.append(num)
            
        if before == after:
            break
        else:
            before = after
            answer += 1
    
    return answer