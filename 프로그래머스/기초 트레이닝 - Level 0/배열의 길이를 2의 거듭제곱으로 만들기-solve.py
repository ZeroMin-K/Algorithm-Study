def solution(arr):
    n = 0
    length = len(arr)
    while length > 2 ** n:
        n += 1
    
    for _ in range(2 ** n - length):
        arr.append(0)
    
    return arr