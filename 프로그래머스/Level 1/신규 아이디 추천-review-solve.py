"""
규칙에 맞지않는 아이디 입력시 유사하면서 규칙에 맞는 아이디 추천
- 아이디 길이 3자이상 15자 이하
- 알파벳 소문자, 숫자, 빼기 - , 밑줄 _, 마침표. 문자만 사용 가능
- 마침표.는 처음과 끝에, 연속 사용불가
처리과정 - 신규유저 아이디 new_id
    1. 모든 대문자를 대응되는 소문자로 치환
    2. 알파벳 소문자, 숫자, 빼기 -, 밑줄_, 마침표. 제외한 모둔 문자 제거
    3. 마침표.가 2번 이상 연속된 부분을 하나의 마침표.로 치환
    4. 마침표.가 처음이나 끝에 위치시 제거
    5. 빈문자열이라면 a 대입
    6. 16자이상이면 첫 15개 문자 제외한 나머지 문자 모두제거
        제거후 마침표.가 끝에 위치하면 끝에 위치한 마침표.문자 제거 
    7. 길이가 2자 이하이면 마지막 문자를 3이 될때까지 반복해서 끝에 붙임 
"""


def solution(new_id):
    answer = ''
    
    # 1. 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower() 
    
    # 2. 알파벳 소문자, 숫자, 빼기 -, 밑줄_, 마침표. 제외한 모둔 문자 제거
    # 문자열 하나씩 탐색하면서 - 문자 ch
    for ch in new_id: 
        # ch가 알파벳이거나 숫자이거나 -, _, . 중에 있으면 정답 문자열에 붙이기
        if ch.isalpha() or ch.isdigit() or ch in ['-', '_', '.']:
            answer += ch
            
    # 3. 마침표.가 2번 이상 연속된 부분을 하나의 마침표.로 치환
    # '..'가 new_id에 있는 동안 
    while '..' in answer:
        # ..를 .으로 replace
        answer = answer.replace('..', '.')
        
    # 4. 마침표.가 처음이나 끝에 위치시 제거
    # new_id[0]이 .인 동안
    while len(answer) > 0 and answer[0] == '.':
        # new_id는 인덱스 1부터 
        answer = answer[1:]
    
    # new_id[-1]이 .인 동안
    while len(answer) > 0 and answer[-1] == '.':
        # new_id는 마지막원소 제외하여 슬라이스 
        answer = answer[:-1]
        
    # 5. 빈문자열이라면 a 대입
    # new_id가 빈문자열이면
    if answer == '':
        # new_id는 a
        answer = 'a'
        
    # 6. 16자이상이면 첫 15개 문자 제외한 나머지 문자 모두제거
    # new_id의 길이가 16이상이면
    if len(answer) >= 16:
        # new_id를 길이 15까지 슬라이스 
        answer = answer[:15]
        
    # 7. 제거후 마침표.가 끝에 위치하면 끝에 위치한 마침표.문자 제거 
    # new_id[-1]이 .인 동안
    while len(answer) > 0 and answer[-1] == '.':
        # new_id를 마지막 문자 제외하여 슬라이스 
        answer = answer[: -1]
        
    # 8. 길이가 2자 이하이면 마지막 문자를 3이i 될때까지 반복해서 끝에 붙임 
    # new_id의 길이가 2자 이하인동안 반복하면서    
    while len(answer) <= 2: 
        # new_id에 new_id[-1]를 붙임 
        answer = answer + answer[-1]
    
    return answer