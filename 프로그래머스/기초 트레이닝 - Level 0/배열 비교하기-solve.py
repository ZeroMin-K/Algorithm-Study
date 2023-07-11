def solution(arr1, arr2):
    answer = 0
    if len(arr2) > len(arr1):
        answer = -1
    elif len(arr2) < len(arr1):
        answer = 1
    else:
        if sum(arr2) > sum(arr1):
            answer = -1
        elif sum(arr2) < sum(arr1):
            answer = 1
    
    return answer