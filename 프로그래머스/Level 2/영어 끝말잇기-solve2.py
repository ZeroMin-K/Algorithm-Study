def solution(n, words):
    # 몇번째 사람이 탈락인지 person 0으로 초기화 
    person = 0
    # 몇번째 차례에서 탈락인지 round 0으로 초기화 
    round = 0
    # 등장한 단어를 넣는 리스트 - words[0] 삽입한상태로 초기화
    words_set = set([words[0]])
    
    # 인덱스 i : 1부터 words의 길이 - 1까지 반복하면서
    for i in range(1, len(words)):
        # 이전 단어의 마지막 글자와 현재 단어의 첫번째 글자가 다르거나 이미 말한 단어라면 
        if words[i - 1][-1] != words[i][0] or \
            words[i] in words_set:
            person = (i % n) + 1
            round = (i // n) + 1
            # 반복 종료
            break 
            
        # 현재 단어를 exists에 삽입
        words_set.add(words[i])

    # [person, round] 리턴
    return [person, round]