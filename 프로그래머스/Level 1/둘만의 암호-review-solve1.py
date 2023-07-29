"""
s, skip: 문자열
index: 자연수
규칙에 따라 문자열 만듬
1. 문자열 s의 알파벳을 index만큼 뒤의 알파벳으로 변경
2. index만큼 뒤의 알파벳이 z를 넘어갈 경우 a로 돌아감
3. skip에 이는 알파벳은 제외하고 건너뜀
return : 변환한 결과 
"""

def solution(s, skip, index):
    alpha_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    alpha_list = [alpha for alpha in alpha_list if alpha not in skip]
    
    password = []
    for alpha in s:
        alpha_index = alpha_list.index(alpha) + index
        password.append(alpha_list[alpha_index % len(alpha_list)])
    
    return ''.join(password)