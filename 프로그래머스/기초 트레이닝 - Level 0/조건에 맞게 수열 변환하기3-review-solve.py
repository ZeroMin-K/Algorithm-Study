def solution(arr, k):
    return [num + k if k % 2 == 0 else k * num for num in arr]