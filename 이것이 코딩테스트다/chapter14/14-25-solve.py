"""
실패율 : 스테이지도달했으나 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수 
N : 전체 스테이지 개수
stages: 게임 이용하는 사용자가 멈춘 스테이지 번호 담긴 배열
return : 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 
"""


def solution(N, stages):
    # 실패율을 담는 리스트 fails 빈리스트로 초기화 
    fails = [] 
    # 스테이지마다 멈춰있는 사용자 수에 대한 리스트 users_in_stages 0을 원소로 길이 N + 1로 초기화 
    users_in_stages = [0] * (N + 2)
    # 총인원 people 은 stages의 길이 
    people = len(stages) 
    
    # stages를 하나씩 탐색하면서 : 원소 stage:
    for stage in stages: 
        # users_in_stages[stage] 1 증가 
        users_in_stages[stage] += 1
        
    # 인덱스 i: 1부터 N까지 반복하면서 - i는 스테이지 번호  
    for i in range(1, N + 1): 
        # 현재 실패율 fail은 people이 0이면 0 아니면 users_in_stages[i] / people
        fail = users_in_stages[i] / people if people != 0 else 0 
        # fails에 (fail, i) 삽입
        fails.append((fail, i)) 
        # people에서 users_in_stages[i] 만큼 감소
        people -= users_in_stages[i] 
    
    # fails를 실패율 내림차순으로 정렬 
    fails.sort(key = lambda x : (-x[0], x[1]))
    
    # fails를 순회하면서 스테이지 번호를 원소로하는 리스트 리턴 
    return [fail[1] for fail in fails]