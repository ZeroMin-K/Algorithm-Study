"""
총 3번의 기회 - 0점에서 10점까지 얻을 수 있음
당첨시 점수에서 1제곱 S, 2제곱 D, 3제곱 T 으로 계산
스타상 * 당첨시 해당 점수와 바로 전에 얻은 점수를 2ㅂ로 만듬
아차상 # 당첨시 해당점수 마이너스
스타상은 첫번째 기회에서 나올수있음. 첫번째 스타상 점수만 2배됨
스타상 효과는 다른 스타상 효과와 중첩 가능. 
스타상, 아차상 중첩 가능 => -2배 
dartResult: 0 ~ 10 정수, S, D, T, *, # 로 구성된 문자열 
총점수를 리턴하기 

문자열을 하나씩 탐색하면서 해당 경우에맞게 점수 계산하면서 진행하기 
"""

def solution(dartResult):
    # 총점 리스트 - 나중에 sum이용해 더할 수 있고 이전 점수 파악가능 
    answer = []
    bonuses = ['S', 'D', 'T']
    
    # dartResult를 한 문자씩 탐색하면서 => score
    for score in dartResult:        
        # 현재 점수가 숫자이면
        if score.isdigit(): 
            # 현재 점수가 0이고 이전 점수가 1이면 (10이 될 경우)
            if score == '0' and len(answer) >= 1 and answer[-1] == 1:
                # 총점리스트에서 pop하고
                answer.pop()
                # 10을 총점리스트에 append
                answer.append(10)
            # 나머지는 
            else:
                # 숫자값을 총점 리스트에 append
                answer.append(int(score))
        # 현재 문자가 보너스나 옵션이면 
        else:
            # 현재 점수는 총점리스트에서 pop한것 
            now = answer.pop()
            # 현재 점수가 (S, D, T)이면
            if score in bonuses: 
                # 현재 점수값을 인덱스에 따라서 +1 하여 제곱함 
                now = now ** (bonuses.index(score) + 1)
            # 현재 점수가 * 이면 
            elif score == '*':
                # 총점리스트에 아무것도 없으면 
                if len(answer) == 0:
                    # 현재 점수만 두배
                    now *= 2
                # 총점리스트에 점수가 존재 하면
                else:
                    # 이전 점수 = 총점리스트에서 pop
                    prev = answer.pop()
                    # 이전 점수 두배로 만들어서 총점리스트에 append
                    answer.append(prev * 2) 
                    # 현재 점수 두배로 만들기 
                    now *= 2
            # 현재 점수가 #이면
            elif score == '#':
                # 현재 점수를 -1배함 
                now *= -1 
            # 현재 점수를 총점리스트에 append 
            answer.append(now)
        
    # 총점 리스트를 sum해서 리턴 
    return sum(answer)