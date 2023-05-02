def solution(num_list):
    sum_total = sum(num_list) ** 2
    mul_total = eval('*'.join([str(n) for n in num_list]))
    
    return 1 if sum_total > mul_total else 0