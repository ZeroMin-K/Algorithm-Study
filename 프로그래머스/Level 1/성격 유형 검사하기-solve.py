"""
4개 지표로 성격 유형 구분. 성격은 각 지표에서 두 유형중 하나로 결정
n개의 질문, 7개의 선택지 
모든 성격유형 점수 더하고 더 높은 점수를 받은 성격 유형이 검사자의 성격유형
점수가 같으면 사전순으로 빠른 성격 유형을 선택
survey: 질문마다 판단하는 지표담은 1차원 문자열배열
    survey[i]의 첫번재 캐릭터는 비동의 선택시 
    survey[i]의 두번째 개릭터는 동의 선택시 
choices: 각 질문마다 선택한 선택지 담은 1차원 정수배열 choices
    매우 동의, 매우 비동의 : 3점 // 동의, 비동의 : 2점 // 약간 동의, 약간 비동의 : 1점 // 모르겠음: 점수X
    1, 2, 3, 4, 5, 6, 7
    1, 2, 3 => survey[i][0] 3, 2, 1
    5, 6, 7 => survey[i][1] 1, 2, 3
return : 성격 유형검사 결과를 지표번호 순서대로 

질문지를 토대로 점수들을 합산하고 
최종적으로 1번지표 R/T, 2번지표 C/F, 3번지표 J/M, 4번지표 A/N에 따라 점수에 맞게 유형 반환 

"""

def solution(survey, choices):
    # 성격 유형 결과 
    answer = ''
    
    # R, T, C, F, J, M , A, N을 키로 하고 값을 0으로 하는 딕셔너리 초기화 
    scores = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    # 인덱스 i: survey의 길이만큼 반복하면서 
    for i in range(len(survey)):
        # 현재 질문 survey[i], 현재 선택 choices[i]
        # choices[i]가 4보다 작으면
        if choices[i] < 4: 
            # 딕셔너리에 survey[i][0]을 키로 하여 값에 4 - choices[i]를 더해줌 
            scores[survey[i][0]] += 4 - choices[i]
        # choices[i]가 4보다 크면
        elif choices[i] > 4:
            # 딕셔너리에 survey[i][1]을 키로 하여 값에 choices[i] - 4를 더해줌 
            scores[survey[i][1]] += choices[i] - 4
            
    # R/T, C/F, J/M, A/N을 하나의 원소로 하는 유형리스트 생성
    types = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    # 유형리스트를 하나씩 반복하면서 - 원소 type 
    for type in types:
        # type[0], type[1]을 키로 딕셔너리의 값을 비교하여 type[0]키의 값이 크거나 같으면
        if scores[type[0]] >= scores[type[1]]:
            # 유형 결과에 type[0]을 붙임
            answer += type[0]
        # 아니면
        else:
            # 유형 결과에 type[1]을 붙임 
            answer += type[1]
    
    return answer