"""
괄호가 바르게 짝지어졌따 => (문자로 열리면 반드시 )문자로 닫힘
문자열 s: (, )로만 이루어진 문자열
문자열s가 올바른 괄호이면 true, 올바르지 않은 괄호이면 false리턴 

문자열 s를 하나씩 읽어가면서 (가 들어오면 +1, )가 들어오면 -1을 진행 
중간에 -1이 되면 바로 return False. 
전부 탐색했을때 0이면 True아니면 False

"""

def solution(s):
    # 괄호를 계산하는 수 total: 0으로 초기화 
    total = 0
    # 문자열 s를 하나씩 탐색하면서 - 원소 bracket
    for bracket in s: 
        # bracket이 (이면
        if bracket == '(': 
            # total에 1을 더함
            total += 1
        # 나머지 (bracket이 )이면)
        else: 
            # total에 1을 뺌 
            total -= 1
            # total이 0보다 작으면
            if total < 0:
                # False 리턴
                return False 
                
    # 전부탐색하고나서 total이 0이면
    if total == 0: 
        # True리턴 
        return True 
    
    # 나머지 경우 False리턴
    return False