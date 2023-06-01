"""
균형잡힌 괄호 문자열 : (, )의 개수가 같음
올바른 괄호 문자열 (, )의 개수가 같고, 짝도 모두 맞음
(, )로만 이루어진 균형잡힌 괄호 문자열 w를 과정을 통해 올바른 괄호 문자열로 변환
1. 입력이 빈문자일 경우, 빈 문자열 반환
2. 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리. u는 더이상 분리 불가능한 균형잡힌 괄호 문자열
3. 문자열 u가 올바른  괄호 문자열이라면 문자열 v에 대해 1단계 부터 다시 수행
    3-1. 수행한 결과를 문자열 u에 이어 붙인 후 반환
4. 문자열 u가 올바른 괄호 문자열이 아니라면 다음 과정 수행
    4-1. 빈문자열에 첫번재 문자로 ( 붙임
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어붙임
    4-3. )를 다시 붙임
    4-4. u의 첫번째, 마지막 문제 제거. 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙임
    4-5. 생성된 문자열 반환
균형 잡힌 괄호 문자열 p를 올바른 괄호 문자열로 변환한 결과를 리턴 
"""

# 문자열 w를 입력 받아서 u,v로 분리하고 u는 더이상 분리 불가능한 균형잡힌 괄호 문자열로 리턴
def seperate(w):
    total = 0
    for i in range(len(w)):
        if w[i] == '(':
            total += 1
        else:
            total -= 1
        
        if total == 0:
            return w[: i + 1], w[i + 1:]
    
    return w, ""

# 문자열s가 올바른 괄호 문자열인지확인하는 함수 
def correct(s):
    total = 0
    for i in range(len(s)):
        if s[i] == '(':
            total += 1
        else:
            total -= 1
            
            if total < 0:
                return False 
            
    if total == 0:
        return True
    
    return False 
    
def solution(p):
    # 입력이 문자열인 경우 
    if p == '':
        # 빈문자열 반환
        return p
        
    # 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리
    # u는 더이상 분리 불가능한 균형잡힌 괄호 문자열
    u, v = seperate(p) 
    # u가 올바른 괄호 문자열 이라면
    if correct(u): 
        # 문자열v에 대해 1단계부터 다시 수행
        v = solution(v) 
        # 수행한 결과를 문자열 u에 이어 붙인 후 반환
        return u + v    
    # u가 올바른 괄호 문자열이 아니라면 
    else: 
        # 빈문자열에 첫번째 문자로 (를 붙임
        answer = '('
        # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어 붙임
        answer += solution(v) 
        # )를 붙임
        answer += ')'
        # u의 첫번째, 마지막 문제 제거
        u = u[1:-1]
        u = list(u)
        # 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙임
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
                
        answer += ''.join(u)
                
        # 생성된 문자열 반환 
        return answer