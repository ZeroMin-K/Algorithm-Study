def solution(order):
    answer = 0
    stacks = [] 
    n = len(order)
    i = 1
    idx = 0
    
    while i < n + 1:
        stacks.append(i)
        while stacks[-1] == order[idx]:
            idx += 1
            stacks.pop()
            if len(stacks) == 0:
                break
                
        i += 1
        
    return idx