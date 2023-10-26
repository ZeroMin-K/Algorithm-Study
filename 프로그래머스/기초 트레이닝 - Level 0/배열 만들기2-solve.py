def solution(l, r):
    answer = [] 
    for i in range(l, r + 1): 
        only_5_and_0 = True
        for num in str(i):
            if num != '5' and num != '0':
                only_5_and_0 = False
                break
        
        if only_5_and_0: 
            answer.append(i) 
            
    return answer if answer else [-1]