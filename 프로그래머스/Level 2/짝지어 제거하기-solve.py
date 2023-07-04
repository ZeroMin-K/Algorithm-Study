"""
s: 알파벳 소문자로 이루어진 문자열
문자열에서 같은 알파벳이 2개 붙어있는 짝찾음
둘을 제거한뒤 앞뒤로 문자열 이어붙임
과정 반복해서 문자열 모두 제거시 종료
성공 수행시 1, 아닐시 0리턴 
"""

def solution(s):
    if len(s) < 2:
        return 0
    
    removed_str = [s[0]]
    for alpha in s[1:]:
        if len(removed_str) > 0 and removed_str[-1] == alpha:
            removed_str.pop()
        else:
            removed_str.append(alpha)
    
    return 1 if len(removed_str) == 0 else 0