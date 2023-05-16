"""
기사 1번부터 number까지 번호 지정 
자신의 기사 번호의 약수 개수에 해당하는 공격력 가진 무기 구매
공격력의 제한수치 정하고 제한수치보다 큰 공격력을 가진 무기 구매하는 기사는 정한 공격력가진 무기를 구매 
공겨력 1당 1kg 철필요 => 무기만들기위한 철무게 계산 
number: 기수단원의 수
제한수치 limit
제한수치 초과한 기사가 사용할 무기 공격력 power
무기를 모두 만들기 위해 필요한 철무게 return 

1부터 number까지 반복하면서
약수개수를 세고 약수 개수가 limit보다 작으면 그대로 증가
크면 power 추가해서 최종합 리턴 

4 => 1, 2, 4
5 => 1, 5 
6 => 1, 2, 3, 6 
8 => 1, 2, 4, 8 
9 => 1, 3, 9 

제곱근까지 구한후 제곱근 기준으로 두배 후 제곱근이 정수이면 1추가

"""
# 약수세는 함수 find_div : 인자 number
def find_div(number):
    # 약수의 개수 total = 0
    total = 0
    # 인덱스 i: 1부터 number의 제곱근까지 반복하면서
    for i in range(1, int(number ** 0.5) + 1):
        # number에 i가 나누어떨어지면
        if number % i == 0:
            # 약수개수 total 1증가
            total += 1
            
    # 약수개수 total 리턴 
    return 2 * total - 1 if int(number ** 0.5) == number ** 0.5 else 2 * total 

def solution(number, limit, power):
    # 최종 무게 
    answer = 0
    
    # 인덱스 i : 1부터 number까지 반복하면서
    for i in range(1, number + 1):
        # 현재 숫자의 약수 개수 세기
        attack = find_div(i)
        
        # 약수개수가 limit 보다 작으면
        if attack <= limit: 
            # 최종무게에 추가
            answer += attack 
        # 약수 개수가 limit보다 크면
        else:
            # 최종무게에 power추가 
            answer += power
    
    return answer