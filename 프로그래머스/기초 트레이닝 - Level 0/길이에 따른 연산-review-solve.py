def solution(num_list):
    answer = num_list[0]
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        for i in range(1, len(num_list)):
            answer *= num_list[i]
            
    return answer