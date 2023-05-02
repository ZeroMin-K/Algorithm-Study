def solution(num_list):
    total = num_list[0]
    for i in range(1, len(num_list)):
        total *= num_list[i]
        
    return 1 if total < (sum(num_list) ** 2) else 0