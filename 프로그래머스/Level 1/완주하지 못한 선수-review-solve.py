"""
단한명 선수 제외하고 모든 선수 마라톤 완주
participant: 마라톤에 참여한 선수 이름 담긴 배열
compeltion: 완주한 선수이름이 담긴 배열 

딕셔너리를 이용하여 participant를 한명씩 탐색하면서 이름을 키로 딕셔너리에 사람이 없으면 값을 1, 있으면 +1을 진행하면서
completion을 하나씩 탐색하여 딕셔너리의 키로 값을 -1 진행
딕셔너리에 값이 0이 아닌것을 반환 
"""

def solution(participant, completion):
    # 참여자 수를 세는 딕셔너리 생성 
    parti_dict = {} 
    # participant를 하나씩 탐색하여 - 원소 person 
    for person in participant: 
        # person이 딕셔너리에 있으면
        if person in parti_dict: 
            # person키로 값을 1 증가
            parti_dict[person] += 1
        # 없으면
        else:
            # person키로 값을 1 
            parti_dict[person] = 1
            
    # completion을 하나씩 탐색하며 - 원소 person
    for person in completion: 
        # 딕셔너리 person키로 값을 -1 감소
        parti_dict[person] -= 1
        
    # 딕셔너리 키, 값을 하나씩 탐색하면서
    for key, value in parti_dict.items():
        # 값이 0이 아니면
        if value != 0:
            # 현재 키 리턴 
            return key