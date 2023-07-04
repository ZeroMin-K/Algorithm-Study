def solution(s):
    answer = [""]
    
    for alpha in s: 
        if answer[-1] == alpha:
            answer.pop()
        else:
            answer.append(alpha)

    return 1 if len(answer) == 1 else 0