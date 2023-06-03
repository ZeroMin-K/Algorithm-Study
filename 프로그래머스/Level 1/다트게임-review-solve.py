"""
3번의 기회 
0점에서 10점까지 얻음
S : 1제곱, D : 2제곱, T : 3제곱 
스타상 * : 해당 점수와 바로 전에 얻은 점수를 각 2배로 만듬
    - 첫번째에 나올수도있으니 이때 첫번째 점수만 2배 
    - 중첩 가능
아차상 # : 해당 점수 마이너스
    - 스타상과 중첩시 -2배 

문자열 입력시 총점수 반환

문자열을 하나씩 읽어가면서 로직에 맞게 처리 후 총점수를 계산 
0점인지 10점인지에 대해서 10점일때 다른 문자로 replace하고 
문자열을 다시 리스트로 변경하면서 이때 다른 문자로 변경된 것을 10으로 변경 
"""

def solution(dartResult):
    # 각 개별 점수를 담는 리스트 - 빈리스트로 초기화 
    answer = []
    
    # dartResult에서 10을 다른 문자 X로 치환
    dartResult = dartResult.replace('10', 'X')
    # dartResult를 리스트 컴프리헨션으로 리스트로 변경하는데 이때 문자 x는 10으로 변경하도록 변경 
    dartResult = ['10' if word == 'X' else word for word in dartResult]
    
    # # dartResult를 하나씩 탐색하면서 - 원소 word
    for word in dartResult:
        # word가 숫자이면 
        if word.isdigit():
            # answer에 append
            answer.append(int(word))
        # word가 숫자가 아니면
        else:
            # 현재 점수는 개별 점수 리스트에서 pop
            now = answer.pop()
            
            # D이면 
            if word == 'D':
                # 현재 점수에서 제곱
                now = now ** 2
            # T이면
            elif word == 'T':
                # 현재 점수에서 세제곱
                now = now ** 3
            # *이면
            elif word == '*':
                # 개별점수 리스트가 현재 비어있지 않으면
                if len(answer) > 0:
                    # 이전 점수 한번더 pop
                    before = answer.pop()
                    # 이전 점수에 2배하고 append
                    answer.append(2 * before)
                # 현재 점수 2배하고 append
                now *= 2
            # #이면
            elif word == '#':
                # 현재 점수 * -1 
                now *= (-1)
                
            # 현재 점수 개별점수에 append
            answer.append(now)
    
    # 개별 점수 리스트의 sum을 반환 
    return sum(answer)