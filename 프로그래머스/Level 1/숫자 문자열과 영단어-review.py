"""
영단어를 숫자로 매칭해서 바꿔주기 
영단어:숫자 문자로 이루어진 사전이 있을때 
사전을 하나씩 탐색하면서 문자열에 맞는게 있으면 맞는 값으로 replace해주기 
"""

def solution(s):
    words = {"zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4', "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'}
    
    for key, value in words.items():
        if key in s:
            s = s.replace(key, value)
    
    return int(s)