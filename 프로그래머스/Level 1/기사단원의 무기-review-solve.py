"""
각 기사 1번부터 number까지 번호 지정
자신의 기사번호의 약수개수에 해당하는 공격력 가진 무개 구매
공격력 제한수치 limit 보다 큰 공격력을 가진 무기 구매시 정한 공격력을 무기 power 구매 
무기는 공격력 1당 1kg 필요 
number: 기사단원수
limit: 제한 수치
power: 제한 수치 초과시 가질 무기 공격력
return : 무기를 모두 만들기 위해 필요한 철의 무게 

무기에 필요한 철의 무게를 0으로 초기화
number부터 약수의 개수를 확인하면서 약수의 개수를 더하고 limit을 넘기면 power를 더함 
약수의 개수를 처음부터 현재자리까지 찾게되면 시간초과 발생 
약수의 개수는 제곱근을 기준으로 대칭구조를 이루므로 제곱근까지 약수의 개수를 찾아서 
대칭시켜 수를 찾음 

4: 1, 2, 4 => 1 * 2 + 1
6: 1, 2, 3, 6 => 2 * 2

"""

def solution(number, limit, power):
    # 필요한 철의 무게 0으로 초기화 
    answer = 0
    
    # 인덱스 i: 1부터 number까지 반복하면서
    for i in range(1, number + 1):
        # 현재 인덱스 i에서 제곱근 왼쪽부분의 개수 left 0으로 초기화 
        left = 0
        # 인덱스 k: 1부터 인덱스i의 제곱근까지 반복하면서  
        for k in range(1, int(i ** 0.5) + 1):
            # i에서 k를 나눴을때 나머지가 0이면
            if i % k == 0:
                # 제곱근 왼쪽부분 개수 left 1증가
                left += 1
                
        # 인덱스 i의 약수 개수 i의 제곱근이 정수이면 left * 2 + 1, 아니면 left * 2를 철의 무게에 더해줌
        div_count = left * 2 - 1 if (i ** 0.5) % 1 == 0 else left * 2
        
        # 인덱스 i의 개수가 limit보다 크면 power를, 아니면 그대로 개수를 철의 무개에 더해줌
        answer += power if div_count > limit else div_count
    
    return answer