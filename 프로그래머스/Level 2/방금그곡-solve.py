"""
음악제목, 재생이 시작되고 끝난 시각, 악보 제공
사용되는 음: C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개 
각음은 1분에 1개씩 재생.
음악은 반드시 처음부터 재생. 음악길이보다 재생된 시간이 길때 음악이 끊김없이 처음부터 반복해서 재생
음악 길이 보다 재생된 시간이 짧은때 처음부터 재생시간만큼만 재생
00:00 넘겨서까지 재생안됨
조건이 일치하는 음악이 여러개일때 라디오에서 재생된 시간이 제일긴 음악제목 반환
    재생된 시간도 같을 경우 먼저 입력된 음악 제목 반환
조건이 일치하는 음악이 없을때 "(None)" 반환 

m: 네오가 기억한 멜로디 담은 문자열
    m: 1개 이상 1439개 이하 
musicinfos: 방송된 곡 정보 배열
    - 100개 이하 곡정보 담긴 배열
    - 음악 시작 시간, 끝난시각, 음악제목, 악보정보가 ,로 구분된 문자열
    - 시작, 끝난시간은 HH:MM 형식
    - 음악제목은 , 이외이ㅡ 출력 가능한 문자로 표현 1이상 64이하 문자열
    - 악보정보는 1개 이상 1439개 이하
return: 조건과 일치하는 음악제목 출력 
"""

# 시작시간, 종료시간 받아서 재생시간 계산하는 함수 
def cal_play_time(start_time, end_time):
    start_hour, start_min = map(int, start_time.split(':'))
    end_hour, end_min = map(int, end_time.split(':'))
    
    return end_hour * 60 + end_min - start_hour * 60 - start_min 

# 음, 악보를 받아서 #음들을 다른 문자로 변경하는 함수 
def convert_sheet(sheet):
    otherSounds = {'C#' : 'H', 'D#' : 'I', 'F#' : 'J', 'G#' : 'K', 'A#' : 'L'}
    for otherSound in otherSounds:
        if otherSound in sheet:
            sheet = sheet.replace(otherSound, otherSounds[otherSound])
    
    return sheet

# 재생시간에 맞게 악보 조정 
def modify_sheet(play_time, sheet):
    length = len(sheet)
    if play_time <= length:
        return sheet[:play_time]
    
    return (sheet * (play_time // length + 1))[:play_time]

def solution(m, musicinfos):
    # 조건에 일치하는 음악 리스트 : 빈리스트로 생성
    answer = [] 
    # 기억한 멜로디 m에서 # 음들 변경 
    m = convert_sheet(m) 
    
    # musicinfos를 enumerate로 하나씩 탐색하면서 : 원소 i, musicinfo
    for i, musicinfo in enumerate(musicinfos): 
        # musicinfo를 ,를 기준으로 시작시간 start, 종료시간 end, 제목 title, 악보 sheet로 분리
        start, end, title, sheet = musicinfo.split(',')
        # 악보 sheet에서 # 음들을 변경 
        sheet = convert_sheet(sheet)
        # 재생시간 play_time 계산
        play_time = cal_play_time(start, end)
        # 재생시간에 맞게 악보 새로 조정 new_sheet
        new_sheet = modify_sheet(play_time, sheet)
        # new_sheet안에 m이 있으면
        if m in new_sheet: 
            # answer에 (i, play_time, title) 삽입
            answer.append((i, play_time, title))
    
    # answer가 비어있으면 "(None)" 리턴
    if not answer: 
        return "(None)"

    # answer을 재생시간 내림차순, 인덱스 오름차순 정렬 후 첫번째원소의 타이틀 리턴 
    answer.sort(key = lambda x: (-x[1], x[0]))
    return answer[0][2]