"""
n : 양의 정수 
n을 k진수로 바꿨을 때 조건에 맞는 소수가 몇개인지
- 0P0처럼 소수 양쪽에 0이 있는 경우
- P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
- 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
- P처럼 소수 양쪽에 아무것도 없는경우
- P는 갓 자릿수에 0을 포함하지 않는 소수
- P는 10진법으로 보았을 때 소수 
return : n을 k진수로 바꿨을 때 변환된 수안에서 찾을 수 있는 조건에 맞는 소수개수 return 
"""
# n을 k진수 문자열로 바꾸는 함수 선언 change_knum : 매개변수 num, k
def change_knum(num, k):
    # 변환한 문자를 저장할 리스트 knums 빈리스트로 생성
    knums = [] 
    
    # num이 k보다 같거나 큰 동안
    while num >= k:
        # num에서 k를 나눈 나머지를 문자열로 변경 후 knums에 삽입
        knums.append(str(num % k))
        # num은 num // k로 갱신
        num //= k
        
    # knums에 num 삽입
    knums.append(str(num))
    # knums를 뒤에서부터 join을 이욯해 문자열로 변환후 리턴 
    knum = ''.join(knums[::-1])
    return knum 

# 소수가 맞는지 확인하는 함수 선언 is_prime : 매개변수 num 
def is_prime(num): 
    if num == 1:
        return False
    # 인덱스 i: 2부터 num의 제곱근까지 반복하면서 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False 
        
    return True
    
def solution(n, k):
    # -- n을 k진수로 바꿈 --
    # n, k를 인자로 change_knum 호출하여 knum에 대입 
    knum = change_knum(n, k) 
    
    # -- k진수로 바꾼 n을 0을 기준으로 분리 --
    # knum을 '0'을 기준으로 분리하고 원소들을 int로 변경한 knums 
    knums = [int(num) for num in knum.split('0') if num ]
    
    # -- 각 분리된 수들이 소수가 맞는지 확인 후 개수 세기 -- 
    # 소수 개수 num_prime 0으로 초기화
    num_prime = 0
    # knums를 하나씩 탐색하면서 : 원소 knum
    for knum in knums: 
        # knum을 인자로 is_prime을 호출하여 True이면
        if is_prime(int(knum)):
            # num_prime 1증가 
            num_prime += 1
    
    # num_prime 리턴 
    return num_prime