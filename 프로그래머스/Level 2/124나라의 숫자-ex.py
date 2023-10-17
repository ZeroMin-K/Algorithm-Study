def solution(n):
    digits = ['1', '2', '4']
    convertedNum = ""
    
    while n > 0:
        n -= 1
        convertedNum = digits[n % 3] + convertedNum
        n //= 3
    
    return convertedNum