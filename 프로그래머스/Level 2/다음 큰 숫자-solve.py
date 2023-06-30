"""
자연수n에 대해 n의 다음 큰 숫자
    1. n의 다음 큰 숫자는 n보다 큰 자연수
    2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 개수 같음
    3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 
"""

def solution(n):
    answer = 0
    # n을 2진수로 변환 후 1의 개수 셈
    n_one_count = bin(n)[2:].count('1')
    # n의 다음 큰 숫자 k는 n + 1로 초기화
    k = n + 1 
    
    # 반복 진행
    while True: 
        # k를 2진수로 변환하여 1의 개수 셈 k_one_count
        k_one_count = bin(k)[2:].count('1') 
        # n_one_count 와 k_one_count가 같으면
        if n_one_count == k_one_count: 
            # 반복종료
            break 
        # 같지 않으면
        else: 
            # k 1증가 
            k += 1
    
    return k