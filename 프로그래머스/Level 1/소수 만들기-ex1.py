from itertools import combinations

def solution(nums):
    answer = 0
    
    for combi in combinations(nums, 3):
        candi = sum(combi)
        for k in range(2, candi):
            if candi % k == 0:
                break
        else:
            answer += 1

    return answer