def solution(arr, intervals):
    return [ num for interval in intervals for num in arr[interval[0] : interval[1] + 1]]