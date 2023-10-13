def solution(arr, queries):
    INF = 1000001
    answer = []
    for s, e, k in queries: 
        min_num = INF
        for i in range(s, e + 1): 
            if arr[i] > k:
                min_num = min(min_num, arr[i])
        answer.append(min_num if min_num != INF else -1)
    return answer