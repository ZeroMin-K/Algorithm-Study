def solution(num_list):
    answer = 0
    mul_total = num_list[0]
    for i in range(1, len(num_list)):
        mul_total *= num_list[i]
    return 1 if mul_total < sum(num_list) ** 2 else 0