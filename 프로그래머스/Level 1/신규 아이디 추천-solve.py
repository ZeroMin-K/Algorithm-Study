"""
규칙에 맞지 않는 아이디 입력시 입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천
아이디 길이는 3자 이상 15자 이하
아이디는 알파벳 소문자, 숫자, 빼기-, 밑줄_, 마침표. 문자만 사용가능
마침표.는 처음과 끝에 사용불가. 연속으로 사용불가

7단계 처리과정으로 이벽한 아이디가 규칙에 맞는지 검사하고 맞지 않는 경우 규칙에 맞는 아이디 추천
1. 모든 대문자를 소문자로 치환
2. 알파벳 소문자, 숫자, 빼기-, 밑줄_, 마침표. 를 제외한 모든 문자제거
3. 마침표.가 2번 이상 연속된 부분을 하나의 마침표.로 치환
4. 마침표.가 처음이나 끝에 위치시 제거
5. 빈 문자열이면 a대입
6. 16자이상이면 첫 15개 문자 제외한 나머지 문자 모두 제거
    - 제거후 마침표.가 끝에 위치하면 끝에 위치한 마침표. 문자 제거
7. 길이가 2자 이하이면, 마지막 문자를 길이가 3이될때까지 반복해서 끝에 붙임 

입력한 아이디 new_id가 매개변수. 7단계 처리과정 거친후 추천 아이디 리턴하기

처리과정 그대로 로직으로 문제 풀이 진행 
"""

def solution(new_id):
    # new_id를 소문자로 변환
    answer = new_id.lower() 
    
    # 알파벳 소문자, 숫자, 빼기-, 밑줄_, 마침표. 를 제외한 모든 문자 제거 
    for word in answer:
        if word.isalpha() or word.isdigit() or word == '-' or word == '_' or word == '.':
            continue
        else:
            answer = answer.replace(word, '')
    
    # ..을 .으로 치환 
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 마침표.가 처음이나 끝에 위치시 제거 
    while len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
        
    while len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]    
        
    # 빈문자열이면 a 대입
    if len(answer) == 0:
        answer = 'a'
        
    # 16자 이상이면 첫 15개 문자 제외한 나머지 문자 모두 제거
    if len(answer) >= 16: 
        answer = answer[:15]
        
    # 제거후 마침표가 끝에 위치하면 끝에 위치한 마침표 . 문자 제거 
    while answer[-1] == '.':
        answer = answer[:-1]
        
    # 길이가 2자 이하면 마지막 문자를 길이가 3이될때까지 반복해서 끝에 붙임
    while len(answer) < 3:
        answer = answer + answer[-1]
        
    return answer