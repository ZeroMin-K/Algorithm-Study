def solution(arr, intervals):
    start1, end1 = intervals[0]
    start2, end2 = intervals[1]
    return arr[start1 : end1 + 1] + arr[start2 : end2 + 1]