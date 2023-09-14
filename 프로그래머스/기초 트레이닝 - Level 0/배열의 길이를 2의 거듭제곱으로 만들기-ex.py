def solution(arr):
    a = 1
    b = len(arr)
    while a < b:
        a *= 2
        
    return arr + [0] * (a - b)