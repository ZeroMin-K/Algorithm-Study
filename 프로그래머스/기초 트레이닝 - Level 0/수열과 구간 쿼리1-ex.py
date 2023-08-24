def solution(arr, queries):
    for s, e in queries:
        arr = [num + 1 if s <= i <= e else num for i, num in enumerate(arr)]
    
    return arr