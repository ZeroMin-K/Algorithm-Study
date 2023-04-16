"""
t에서 p와 길이가 같은 부분 문자열 중에서 부분문자열 수가 p보다 작거나 같은 경우를 하나씩 세서 진행 
"""

def solution(t, p):
    answer = 0
    # p의 길이 
    end = len(p) 
    
    # 인덱스 i - 0부터 len(t)에서 p길이만큼 반복하면서
    for i in range(len(t) - end + 1):
        # t[i: i + end]를 숫자로 변환하여 p보다 작으면 
        if int(t[i: i + end]) <= int(p):
            # answer 증가 
            answer += 1
    
    return answer