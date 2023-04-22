"""
처음나오는 글자는 -1
현재 인덱스에서 이전에 나왔던 글자의 인덱스를 빼서 정답 표시 
현재 위치를 저장 
문자열을 하나씩 탐색하면서 진행하기 
"""

def solution(s):
    answer = []
    
    # 글자를 저장하는 사전 
    words = dict() 
    
    # 인덱스 i를 0부터 s의 문자열길이만큼 반복하면서  
    for i in range(len(s)):
        # s[i]가 사전에 없으면
        if s[i] not in words:
            # -1을 정답 리스트에 append
            answer.append(-1)
        # s[i]가 사전에 있으면
        else:
            # i에서 s[i]의 사전에 대한 키값을 빼서 정답 리스트에 append
            answer.append(i - words[s[i]])
        # s[i]를 사전에 값을 i로 저장 
        words[s[i]] = i

    return answer