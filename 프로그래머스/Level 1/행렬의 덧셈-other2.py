def solution(arr1, arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]