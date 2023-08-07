def solution(binomial):
    x, op, y = binomial.split()
    
    x, y = int(x), int(y)
    
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    else:
        result = x * y
    
    return result