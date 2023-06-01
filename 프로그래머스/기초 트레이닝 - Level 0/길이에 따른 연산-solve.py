def solution(num_list):
    if len(num_list) >= 11:
        answer = sum(num_list)
    else:
        answer = num_list[0]
        for i in range(1, len(num_list)):
            answer *= num_list[i]
            
    return answer