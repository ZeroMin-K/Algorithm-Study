"""
실패율 = 스테이지 도달했으나 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수 
전체 스테이지 개수 n, 스테이번호 담긴 배열 stages 
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 담긴 배열 리턴 
N + 1은 마지막 스테이지까지 클리어한 사용자 
실패율 같으면 작은 번호 스테이지가 먼저 오도록함 
스테이지 도달한 유저 없으면 실패율 0

"""

def solution(N, stages):
    answer = []
    
    # 각 스테이지 도달한 사용자 수 세는 리스트 생성 길이는 N + 2 (N + 1 인덱스는 마지막 스테이지까지 도달 )
    clears = [0] * (N + 2) 
    
    # stages를 하나씩 탐색하면서 
    for stage in stages:
        # 각 스테이지마다 클리어하지 못한 사용자 숫자 세기 
        clears[stage] += 1
        
    # 실패율 리스트 초기화 
    fails = [] 
    # 총 사용자 수 stages 길이 
    total = len(stages)
    # 1번 스테이지부터 확인하면서 
    for i in range(1, N + 1):
        # 실패율 계산 : 현재 스테이지 사용자 / 총 사용자수 
        if total != 0:
            fail_ratio = clears[i] / total 
        else:
            fail_ratio = 0
            
        # 총 사용자에서 현재 스테이지 사용자 빼기 
        total -= clears[i] 
        # 실패율 리스트에 (실패율, 스테이지번호)로 append
        fails.append((fail_ratio, i))
        
    # 실패율 리스트 실패율 내림차순, 스테이지번호 오름차순으로 정렬 
    fails.sort(key = lambda x: (-x[0], x[1]))
    # 실패율 리스트를 스테이지 번호만으로 리스트 새로 생성해서 리턴 
    return [fails[i][1] for i in range(len(fails))]