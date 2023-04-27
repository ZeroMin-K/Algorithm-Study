def solution(k, score):
    answer = []
    
    q = []
    for s in score:
        q.append(s)
        if len(q) > k:
            q.remove(min(q))
        answer.append(min(q))
    
    return answer