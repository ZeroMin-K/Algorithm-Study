def solution(arr, idx):
    new_arr = [index for index, value in enumerate(arr) if index >= idx and value == 1]
    return -1 if len(new_arr) == 0 else new_arr[0]