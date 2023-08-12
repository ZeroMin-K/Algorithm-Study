"""
균형잡힌 문자열: (와 )의 개수가 같은 문자열 
올바른 괄호 문자열: (와 )의 개수가 같고 짝도 모두 맞는 문자열 
균형잡힌 괄호 문자열 w를 올바른 괄호 문자열로 변환
    1. 입력이 빈 문자열인 경우 빈문자열 반환
    2. 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리
        - u는 더이상 분리 불가, v는 빈문자열 가능 
    3. 문자열 u가 올바른 괄호 문자열이면 문자열 v에 대해 1단계부터 다시 수행
        3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반호나
    4. 문자열 u가 올바른괄호 문자열이 아니라면
        4-1. 빈 문자열에 첫번째 문자로 ( 붙임
        4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어 붙임
        4-3. )를 다시 붙임
        4-4. u의 첫번째와 마지막 문자 제거. 나머지 문자열의 괄호 방향 뒤집어서 뒤에 붙임
        4-5. 생성된 문자열 반환
p: 균형 잡힌 괄호 문자열
return : 올바른 괄호 문자열로 변환한 결과 
    p가 이미 올바른 괄호문자열이면 그대로 리턴
"""
# 문자열을 균형잡힌 괄호 문자열 두개로 분리하는 메서드 seperate - 매개변수 w
def seperate(w):
    total = 0
    index = 0 
    for i in range(len(w)):
        if w[i] == '(':
            total += 1
        else:
            total -= 1
        
        if total == 0:
            index = i
            break
            
    return w[: i + 1], w[i + 1:]

# 문자열이 올바른 괄호 문자열인지 확인하는 메서드 check_correct - 매개변수 w
def check_correct(w):
    total = 0
    is_correct = True 
    for i in range(len(w)):
        if w[i] == '(':
            total += 1
        else:
            total -= 1
            
        if total < 0:
            is_correct = False
            break 
            
    if total != 0:
        is_correct = False

    return is_correct 

def solution(p):
    answer = ''
    
    # 입력이 빈 문자열인 경우 빈문자열 반환
    if len(p) == 0:
        return '' 
    # 문자열 p를 두 균형잡힌 괄호 문자열 u, v로 분리
    u, v = seperate(p) 
    # 문자열 u가 올바른 괄호 문자열이면 
    if check_correct(u):
        #문자열 v에 대해 1단계부터 다시 수행
        v = solution(v)
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환
        answer = u + v 
    # 문자열 u가 올바른괄호 문자열이 아니라면
    else:
        # 빈 문자열에 첫번째 문자로 ( 붙임
        answer = '('
        # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열 이어 붙임
        answer += solution(v) 
        # )를 다시 붙임
        answer += ')'
        # u의 첫번째와 마지막 문자 제거. 
        u = u[1:-1]
        # u의 나머지 문자열의 괄호 방향 뒤집어 answer뒤에 붙임 
        for char in u: 
            if char == '(':
                answer += ')'
            else:
                answer += '('
    
    return answer