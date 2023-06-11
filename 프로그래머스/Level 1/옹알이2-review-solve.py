"""
"aya", "ye", "woo", "ma" 네가지 발음과 네가지 발음을 조합해서만들 수 있는 발음만 가능
연속으로도 발음 불가 
babbling: 문자열 배열
return : 조카가 발음할 수 있는 단어 개수 리턴 

발음을 연속으로 할수있는 것들이 있으면 제외하고
할수있는 발음들을 다른 글자로 변경하면서 전부 변경했을때 남은 문자가 있으면 발음할수없는 문자.
남은문자가없으면 발음할 수 있는 문자 

"""
def solution(babbling):
    # 발음할 수 있는 단어의 개수 0으로 초기화 
    answer = 0
    
    # 네가지 발음 리스트 speaks 
    speaks = ["aya", "ye", "woo", "ma"]
    
    # babbling을 하나씩 탐색하면서 - 원소 word
    for word in babbling: 
        # 네가지 발음리스트를 하나씩 탐색하면서 - 원소 speak 
        for speak in speaks: 
            # speak + speak가 word에 있으면 발음불가
            if speak + speak in word:
                break
            
            # speak + speak가 word에 없는 동안 - 연속으로 발음 불가
            while speak in word: 
                # word의 speak를 빈문자열 ''로 변경
                word = word.replace(speak, '')
                
        # word가 빈문자열이면
        if len(word) == 0:
            # 발음할 수 있는 단어 개수 1 증가 
            answer += 1
    
    return answer