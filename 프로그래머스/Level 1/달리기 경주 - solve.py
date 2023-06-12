"""
해설진들은 선수들이 자기 바로 앞의 선수를 추월할때 추월한 선수의 이름 부름 
players: 선수 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열
callings: 해설진이 부른 일므을 담은 문자열 배열
return : 경주 끝났을때 선수들의 이름을 1등부터 등수 순서대로의 배열 

callings를 하나씩 탐색하면서 부른 선수가 players에서 k등일때 k - 1등으로 변경, k-1등은 k등으로 변경 

callings 최대 길이 1,000,000 * players 최대 길이 50,000 => 50,000,000,000 
이름을 불렀을때 등수를 알아야하고 해당 등수 -1이 누구인지도 알아야함
이름:등수, 등수:이름 두개의 딕셔너리 이용해서 풀이 
"""

def solution(players, callings):
    # 등수 => 선수이름의 딕셔너리 초기화
    score_to_name = {i + 1: name for i, name in enumerate(players)} 
    # 선수 이름 => 등수의 딕셔너리 초기화 
    name_to_score = {name: i + 1 for i, name in enumerate(players)} 
        
    # callings를 하나씩 탐색하면서 - 원소 calling (현재 추월한 선수 이름)
    for calling in callings: 
        # calling을 값으로 하여 현재 추월한 선수의 등수 score를 찾음 
        score = name_to_score[calling]
        # score - 1 등의 선수 이름을 찾음
        competitor = score_to_name[score - 1]
        
        # 해당 선수를 score등으로 변경
        name_to_score[competitor] = score
        score_to_name[score] = competitor 
        
        # 현재 추월한 선수를 score -1 등으로 변경 
        name_to_score[calling] = score -1
        score_to_name[score - 1] = calling
        
    # 최종 경주 결과 배열 
    # 인덱스 i: 1부터 players 길이만큼 반복하면서 인덱스 i등에 해당하는 선수들을 경주 결과배열에 반환 
    answer = [score_to_name[i] for i in range(1, len(players) + 1)]
        
    return answer