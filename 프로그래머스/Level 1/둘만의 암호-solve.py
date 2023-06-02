"""
문자열s, 문자열 skip, 자연수 index. 규칙에 따라 문자열 만듬
1. 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 변경
2. index 만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아감
3. skip에 있는 알파벳은 제외하고 건너뜀 

변환한 결과를 담을 빈 문자열에 문자열 s의 문자를 하나씩 탐색하면서
index만큼 알파벳으로 변경하고 skip에 있는 알파벳은 제외하여 바뀐 문자를 빈문자열에 붙여서 반환 
"""

def solution(s, skip, index):
    # 변환한 결과를 담은 빈 문자열 
    answer = ''
    
    # skip의 원소들을 아스키코드로 변환한 리스트 new_skip
    new_skip = [ord(i) for i in skip]
    
    # 문자열 s를 하나씩 탐색하면서 - 원소 문자: alpha 
    for alpha in s:
        # 변경할 문자의 아스키코드 new_alpha는 alpha의 아스키코드 
        new_alpha = ord(alpha) 
        # index만큼 반복을 진행하면서 
        for _ in range(index):
            # 변경할 문자의 아스키 코드 new_alpha 1 증가 
            new_alpha += 1
            # 변경할 문자의 아스키 코드 new_alpha가 z의 아스키코드보다 크면
            if new_alpha > ord('z'): 
                # 변경할 문자의 아스키 코드 new_alpha는 a의 아스키코드 
                new_alpha = ord('a')
            
            # new_skip리스트안에 변경할 문자의 아스키 코드 new_alpha 원소와 같은 값이 있는 동안 
            while new_alpha in new_skip:
                # 변경할 문자 아스키 코드 new_alpha 1 증가 
                new_alpha += 1
                # 변경할 문자의 아스키 코드 new_alpha가 z의 아스키 코드보다 크면
                if new_alpha > ord('z'):
                    # 변경할 문자의 아스키 코드 new_alpha는 a의 아스키 코드
                    new_alpha = ord('a')
                
        # answer에 new_alpha를 문자로 변경하여 붙임 
        answer += chr(new_alpha)
         
    return answer