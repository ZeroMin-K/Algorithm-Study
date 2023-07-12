def solution(arr, n):
    return [arr[i] if i %  2 == 0 else arr[i] + n for i in range(len(arr))] \
            if len(arr) % 2 == 0 else \
            [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))]