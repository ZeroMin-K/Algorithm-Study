def solution(babbling):
    # 발음 가능한 단어 수 
    answer = 0
    
    # 가능한 4가지 발음 리스트 
    speaks = ["aya", "ye", "woo", "ma"]
    
    # babbling 문자열 배열 하나씩 탐색하면서 - 원소 word
    for word in babbling:
        # 4가지 발음 리스트 하나씩 탐색하면서 - 원소 speak 
        for speak in speaks:
            # 연속된 같은 발음이 없다면 
            if speak * 2 not in word:
                # word의 해당 발음을 ' '으로 치환 
                word = word.replace(speak, ' ')
        # 치환이 끝난 문자열의 공백을 제거했을때 빈 문자열과 같다면 
        if word.strip() == '':
            # 발음 가능한 단어 수 증가 
            answer += 1
    return answer