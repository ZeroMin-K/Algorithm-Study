def solution(binomial):
    expressions = binomial.split()
    answer = int(expressions[0])
    y = int(expressions[2])
    op = expressions[1]
    
    if op == '+':
        answer += y
    elif op == '-':
        answer -= y
    elif op == '*':
        answer *= y
    else:
        answer /= y
        
    return answer