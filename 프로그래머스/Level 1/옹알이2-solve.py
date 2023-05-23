"""
aya, ye, woo, ma 네가지 발음과 조합해서 만들수 있는 발음
연속해서 같은 발음 어려움
문자열 배열 babbling이 매개변수로 주어질때 발음할 수 있는 단어 개수 리턴 

일부 일치가 아니라 조합했을 때 완전히 일치하는 단어들만 가능 

네가지 발음 리스트를 하나씩 탐색하면서 문자열에 해당 발음을 빈문자열로 변경하는식으로 진행하여
최종적으로 빈문자열이 되면 변경가능하고 되지않으면 발음불가 

"""

def solution(babbling):
    # 발음할 수 있는 단어 개수 
    answer = 0
    
    # 네가지 발음 리스트 
    langs = ["aya", "ye", "woo", "ma"]
    
    # 인덱스 i - 0부터 babbling의 길이 - 1까지 반복하면서 
    for i in range(len(babbling)):
        # 네가지 발음 리스트 하나씩 탐색하면서 - 원소 lang
        for lang in langs: 
            # babbling[i]안에 발음리스트가 있으면
            if lang in babbling[i]:
                # babbling[i]에서 lang부분을 ''문자열로 변경함
                babbling[i] = babbling[i].replace(lang, '')
        
        # babbling[i]의 길이가 0이면
        if len(babbling[i]) == 0:
            # 발음할 수 있는 단어개수 1 증가 
            answer += 1
        
    return answer