"""
올바른 괄호 문자열
- (), [], {} 올바른 괄호 문자열
- A가 올바른 괄호문자열이면 (A), [A], {A}도 올바른 괄호 문자열
- A,B가 올바른 괄호문자열이면 AB도 올바른 괄호 문자열 
=> (), [], {}만 잘 지켜지면 감싸도, 옆으로 합쳐도 올바른 괄호 문자열 
s : 대괄호, 중괄호, 소괄호로 이루어진 문자열
return : s를 왼쪽으로 x칸만큼 회전시 s가 올바른 괄호 문자열이 되게하는 x의 개수 

s를 왼쪽으로 0부터 최대 s의 길이 -1 만큼 회전하면서 올바른 괄호 문자열인지 확인하여 x의 개수 세기 
왼쪽으로 이동하는것을 굳이 이동할 필요없이 s를 두개 나란히 붙여서 인덱스만 이동하기
올바른 괄호문자열은 스택을 활용하여 
    각 서로 맞는 닫힌 문자열이 나오면 pop하여 최종적으로 스택이 비어있는지 아닌지로 판단 
"""

def solution(s):
    # x칸 옮길시 올바른 괄호 문자열인 개수 answer 0으로 초기화 
    answer = 0
    # (), [], {} 에 대한 딕셔너리 bracket_dict 키는 닫힌 문자열, 값은 열린 문자열
    bracket_dict = {')' : '(', ']' : '[', '}' : '{'}
    
    # s를 두개 붙인 extended_s
    extended_s = s + s 
    # 인덱스 i : 0부터 s의 길이 - 1만큼 반복하면서 
    for i in range(len(s)): 
        # 현재 이동한 문자열 rotated_s 는 extended_s에서 i부터 i + s의 길이 만큼 슬라이싱한 문자열
        rotated_s = extended_s[i: i + len(s)]
        # 현재 rotated_s에 대한 스택 stack 빈 리스트로 초기화
        stack = [] 
        # rotated_s를 하나씩 탐색하면서 : 원소 bracket 
        for bracket in rotated_s: 
            # bracket이 열린 괄호이면 stack에 삽입 
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            # stack의 길이가 0보다 크고 stack의 마지막원소와 backet_dict[bracket]과 같으면
            elif len(stack) > 0 and stack[-1] == bracket_dict[bracket]:
                # stack pop
                stack.pop()
            # 나머지의 경우 전부 stack에 삽입 
            else:
                stack.append(bracket)
                
        # stack이 비어있으면
        if len(stack) == 0:
            # answer 1증가 
            answer += 1
    
    return answer