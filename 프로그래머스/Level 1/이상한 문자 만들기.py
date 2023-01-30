"""
공백기준으로 문자열 리스트를 만들어 문자열 리스트를 하나씩 탐색하여 
각 단어들을 바꾸기 
이후 공백으로 join
"""
def solution(s):
    # 결과 문자열 리스트 생성
    answer = []
    # 공백기준으로 문자열 리스트 생성
    words = list(s.split(' '))
    # 문자열 리스트 하나씩 반복하며
    for word in words:
        # 현재 문자열에 대한 임시 리스트 생성 
        temp = []
        # 문자열 하나씩 인덱스 0부터 반복하면서
        for i in range(len(word)):
            # 현재 인덱스에 해당하는 문자가 홀수 이면
            if i % 2 == 1:
                # 소문자로
                temp.append(word[i].lower())
            # 짝수이면 
            else:
                # 대문자로 
                temp.append(word[i].upper())
            
        # 문자열이 완성된 임시리스트를 결과 문자열로 append
        answer.append(''.join(temp))
        
    # 공백으로 결과 문자열 리스트 join
    return ' '.join(answer)