def solution(a, d, included):
    answer = 0
    for i, v in enumerate(included):
        answer += (a + d * i) * int(v)
    return answer