def solution(arr):
    is_2_in = False
    start = 0
    end = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] == 2:
            start = i
            is_2_in = True 
            break
            
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 2:
            end = i
            break
            
    return arr[start : end + 1] if is_2_in else [-1]