# 균형 잡힌 괄호 문자열의 인덱스 반환 
def balanced_index(p):
    count = 0       # 왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0       # 왼쪽 괄호 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            # 쌍이 맞지 않는 경우 False 반환
            if count == 0:      
                return False 
            count -= 1
            
    # 쌍이 맞는 경우 True 반환
    return True 

def solution(p):
    answer = ''
    if p == '':
        return answer
    
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    # 올바른 괄호 문자열이면 v에 대해 수행한 결과 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 다음 과정 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        # 첫번째와 마지막 문자 제거
        u = list(u[1 : -1])    
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    
    return answer