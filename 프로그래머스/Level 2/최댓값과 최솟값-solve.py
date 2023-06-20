"""
s: 공백으로 구분된 숫자들이 저장된 문자열
return : s에 나타나는 숫자 중 최소값, 최대값을 찾아  "(최솟값) (최댓값)" 형태 문자열로 반환
"""

def solution(s):
    s = [int(num) for num in list(s.split())]
    return str(min(s)) + " " + str(max(s))