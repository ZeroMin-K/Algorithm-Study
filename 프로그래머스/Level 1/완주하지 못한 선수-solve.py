"""
단 한명 선수 제외하고 모든 선수 마라톤 완주
participant: 마라톤에 참여한 선수들의 이름이 담긴 배열
completion: 완주한 선수들의 이름 담긴 배열
완주하지 못한 선수의 이름 리턴 
동명이인이 있을 수 있음=> 두명이 참가해서 한명은 완주하고 한명은 완주 못할 수 있음 

참가자 선수들을 한명씩 딕셔너리에 넣으면서 숫자를 증가시킴
딕셔너리에 없으면 1, 있으면 +1
완주한 선수들 한명씩 넣으면서 -1을 진행 
딕셔너리안에 0보다 큰게 완주 못한 선수 
"""

def solution(participant, completion):
    answer = ''
    
    # 참가자 선수를 담을 딕셔너리 participant_dict
    participant_dict = dict() 
    
    # participant 하나씩 탐색하면서 - 원소 person
    for person in participant:
        # 딕셔너리안에 있으면 
        if person in participant_dict: 
            # [person] + 1
            participant_dict[person] += 1
        # 없으면
        else: 
            # [person] 1
            participant_dict[person] = 1
            
    # completion하나씩 탐색하면서 - 원소 person
    for person in completion: 
        # [person]을 -1 진행
        participant_dict[person] -= 1
        
    # dict를 하나씩 탐색하면서
    for person, value in participant_dict.items(): 
        #0보다 큰게 완주못한 선수 
        if value > 0: 
            answer = person 
            
    return answer