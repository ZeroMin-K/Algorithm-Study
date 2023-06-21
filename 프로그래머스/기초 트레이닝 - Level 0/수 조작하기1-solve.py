def solution(n, controls):
    
    control_dict = {"w" : 1, "s" : -1, "d" : 10, "a" : -10}
    
    for control in controls: 
        n += control_dict[control]
        
    return n