from itertools import combinations

def solution(numbers):
    answer = []
    for combi in list(combinations(numbers, 2)):
        if sum(combi) not in answer:
            answer.append(sum(combi))
    answer.sort()
    return answer