"""
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하기 
"""

def solution(strings, n):
    strings.sort(key = lambda x: (x[n], x))
    return strings