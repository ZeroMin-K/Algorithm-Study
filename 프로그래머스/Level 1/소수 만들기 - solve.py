"""
배열에서 3개 수를 뽑아서 더한다음 이숫자가 소수인지 확인하기
소수이면 개수 증가 
"""

from itertools import combinations 
import math 

# 소수인지 확인하는 함수 선언 - 매개변수 숫자 number, 소수 리스트 primes 
def find_primes(number, primes):
    # 현재 숫자 number가 False이면 (primes[number])
    if not primes[number]:
        # False return 
        return False
        
    # 인덱스 i - 2부터 number의 제곱근까지 반복하면서 
    for i in range(2, int(math.sqrt(number)) + 1):
        # 곱할 수 k = 2
        k = 2
        # i * k 가 number보다 작은 동안
        while i * k <= number:
            # primes에서 인덱스 i * k = False
            primes[i * k] = False
            # k에 1증가
            k += 1
    
    # number가 소수면 primes 원소로 True리턴, 아니면 False리턴 
    return primes[number]
    
def solution(nums):
    # 소수의 개수 
    answer = 0
    
    # 배열에서 3개를 뽑아서 전부 더했을 때 최대의 합으로 길이로 소수인지 여부 판단하는 리스트
    # 1000 + 1000 + 1000이 최대 크기 전부 True로 초기화 
    primes = [True] * (3001)
    # 숫자 1은 소수가 아님 
    primes[1] = False 
    
    # combination을 이용해 3개를 뽑아서 리스트로 만들어서 하나씩 탐색하며
    for combi in list(combinations(nums, 3)):
        # 3개를 더해서 소수이면
        if find_primes(sum(combi), primes):
            # 개수 answer에 1증가
            answer += 1

    return answer