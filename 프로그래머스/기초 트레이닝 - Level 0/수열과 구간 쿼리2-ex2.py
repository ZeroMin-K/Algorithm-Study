def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = [i for i in arr[s: e + 1] if i > k]
        answer.append(min(tmp) if tmp else -1)
    return answer