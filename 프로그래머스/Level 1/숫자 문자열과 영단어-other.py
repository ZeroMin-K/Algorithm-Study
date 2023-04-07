"""
각 영단어를 키를 가지고 값으로 숫자 문자를 가지는 사전 생성
각 사전들의 키를 하나씩 탐색하면서 문자열 안에 있으면
새로운 문자열에 해당 값을 붙여서 문자열을 숫자로 변환 
"""

def solution(s):
    # 영단어를 키로 가지고 값을 숫자로 가는 사전 
    words = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
    
    # 사전의 키를 하나씩 탐색하면서
    for key, value in words.items():
        # 문자열에서 해당키를 문자열로 변경 
        s = s.replace(key, value )
    return int(s)