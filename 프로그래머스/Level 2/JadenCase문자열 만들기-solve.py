"""
JadenCase: 모든 단어의 첫문자가 대문자. 그외 알파벳은 소문자 
첫문자가 알파벳이 아닐대 이어지는 알파벳은 소문자로 사용 
return : 문자열 s를 JadenCase로 바꾼 문자열
"""

def solution(s):
    # 변경할 문자 
    answer = '' 
    # 단어의 첫문자인지 여부 first True로 초기화 
    first = True 
    # 인덱스 i: 0부터 s의 길이 -1만큼 반복하면서
    for i in range(len(s)):
        # 현재 문자 
        now = s[i]
        
        # s[i]가 공백이면
        if now == ' ':
            # 다음에 나타나는 글자는 단어의 첫문자 First를 True로 초기화
            first = True 
        # s[i]가 알파벳일때  
        elif now.isalpha(): 
            # first가 True이면 (단어의 첫문자 이면)
            if first: 
                # s[i]는 s[i]를 대문자로 바꾼 것 
                now = now.upper() 
                # First를 False로 변경 
                first = False 
            # first가 False이면(단어의 첫문자가 아니면)
            else:
                # 소문자로 변경
                now = now.lower() 
        # 나머지 경우 
        else:
            first = False 
                
        answer += now 
    return answer