"""
combination을 이용하여 두개 수를 뽑은 후 더해서 리스트에 넣고 
세트로 만들고 다시 리스트로 만들어 오름차순으로 정렬하고 리턴 
"""
from itertools import combinations

def solution(numbers):
    answer = []
    for combi in combinations(numbers, 2):
        answer.append(sum(combi))
    return sorted(list(set(answer)))