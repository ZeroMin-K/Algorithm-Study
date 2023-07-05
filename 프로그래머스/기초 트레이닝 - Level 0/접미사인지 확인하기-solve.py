def solution(my_string, is_suffix):
    if len(is_suffix) > len(my_string):
        return 0 
    
    return 1 if my_string[len(my_string) - len(is_suffix):] == is_suffix else 0