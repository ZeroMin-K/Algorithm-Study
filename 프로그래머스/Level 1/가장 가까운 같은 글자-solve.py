"""
문자열 s에서 각 문자를 하나씩 탐색하면서 처음 나오면 -1, 이전에 나왔으면 가장 가까운 글자 얼마나 떨어졌는지 리스트에 더하기
각 문자를 dict 안에 현재 인덱스를 넣으면서 dict에 없으면 -1 dict에 있으면 현재 인덱스값과 dic의 차이를 
결과 리스트에 더하고 현재 인덱스값을 dict에 갱신 

"""

def solution(s):
    answer = []
    
    freqs = dict()
    
    for i in range(len(s)):
        if s[i] not in freqs.keys():
            freqs[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - freqs[s[i]])
            freqs[s[i]] = i
            
    return answer