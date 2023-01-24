def solution(s):
    for num in s:
        if not s.isdigit():
            return False
    
    if len(s) == 4 or len(s) == 6:
        return True
    else:
        return False