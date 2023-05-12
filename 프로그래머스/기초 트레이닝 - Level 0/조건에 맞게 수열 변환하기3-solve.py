def solution(arr, k):
    return [num + k for num in arr] if k % 2 == 0 else [num * k for num in arr]