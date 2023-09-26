def solution(strArr):
    answer = [0] * 31
    for str in strArr:
        answer[len(str)] += 1
    
    return max(answer)