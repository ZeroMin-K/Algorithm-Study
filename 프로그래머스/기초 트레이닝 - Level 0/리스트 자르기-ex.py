def solution(n, slicer, num_list):
    a, b, c = slicer
    answer = [] 
    
    if n == 1:
        answer = num_list[:b + 1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a : b + 1]
    elif n == 4:
        answer = num_list[a : b + 1 : c]
        
    return [num_list[:b + 1],
            num_list[a:],
            num_list[a : b + 1],
            num_list[a : b + 1 : c]
    ][n - 1]