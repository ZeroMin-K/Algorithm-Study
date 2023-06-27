def solution(num_list):
    num_list.sort() 
    return [num_list[i] for i in range(5, len(num_list))]