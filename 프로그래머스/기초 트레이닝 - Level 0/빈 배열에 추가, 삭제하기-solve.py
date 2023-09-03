def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            for _ in range(2 * arr[i]):
                answer.append(arr[i]) 
        else:
            for _ in range(arr[i]):
                answer.pop()
            
    return answer