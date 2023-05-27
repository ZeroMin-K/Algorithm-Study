# 소수인지 확인하는 함수 선언 - 매개변수 num, 숫자들 소수인지 확인하는 딕셔너리 primes 
def check_prime(num, primes):
    
    # 현재 num이 소수가 아니면 
    if num in primes and not primes[num]:
        # False 리턴
        return False
        
    # 인덱스 i - 2부터 num의 제곱근까지 확인하면서
    for i in range(2, int(num ** 0.5) + 1):
        # 인덱스 j = 2
        j = 2
        # i * j 가 num보다 작은 동안
        while (i * j) <= num:
            # primes[i * j] = false 소수가 아님
            primes[i * j] = False
    
    if num not in primes:
        primes[num] = True 
        
    # num에 대한 primes 리턴 
    return primes[num]

def solution(nums):
    answer = -1
    # 숫자들 소수인지 확인하는 딕셔너리 primes (소수면 true, 아니면 false)
    primes = dict() 
    # 2,3은 소수 
    primes[2] = True
    primes[3] = True
    
    # 소수가 되는 경우에 대한 리스트 
    total_primes = [] 
    
    from itertools import combinations
    # nums를 combinations으로 3개를 뽑안 경우의수를 하나씩 탐색하면서
    for combi_case in list(combinations(nums, 3)):
        # 해당 케이스들을 합했을 때 소수가 되면
        if check_prime(sum(combi_case), primes):
            # 소수가 되는 경우의 수 추가 
            total_primes.append(sum(combi_case))

    # 소수가 되는 경우에 대한 리스트를 set로 변환 후 다시 list로 변경한 다음 길이 리턴 
    return len(list(set(total_primes)))