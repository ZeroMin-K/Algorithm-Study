"""
균형잡힌 괄호 문자열 - (, ) 개수 같다
올바른 괄호 문자열 - (, ) 개수 같고 짝도 맞다
(,)로만 이루어진 문자열 w가 균형잡힌 괄호 문자열이면 올바른 괄호 문자열로 변환

균형잡힌 괄호 문자열 p => 올바른 괄호 문자열로 변환한 결과 리턴 
"""

# 올바른 괄호 문자열인지 확인
def check_correct(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

# 두 균형잡힌 문자열 u, v로 분리
def seperate(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return w[:i+1], w[i+1:]
            
def solution(p):
    answer = ''
    
    if len(p) == 0:
        return ''
        
    # 균형잡힌 문자열 p를  두 균현장힙 문자열 u, v로 분리
    u, v = seperate(p)
    
    # u가 올바른 괄호 문자열이면
    if check_correct(u):
        # v에 대해서 다시 진행
        v = solution(v)
        # u에 v를 붙여서 반환
        return u + v
    # u가 올바른 괄호 문자열이 아니면
    else:
        # 빈문자열에 첫번째 문자로 ( 붙임
        answer += '('
        # 문자열 v에 대하여 다시 수행하고 문자열 붙이기
        answer += solution(v)
        # ) 다시 붙이기
        answer += ')'
        
        # u의 첫번째 , 마지막 문자 제거하고 , 나머지 문자열의 괄호 방향을 뒤집어 붙임
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
                
    # 생성된 문자열 반환 
    return answer