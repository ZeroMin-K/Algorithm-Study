"""
피로도 시스템: 0 이상의 정수. 일정 피로도 사용해 던전 탐험 
최소 필요 피로도: 던전 탐험위해 가지고있어야하는 최소한 피로도
소모 피로도: 던전 탐험 후 소모되는 피로도 
하루에 한번씩 탐험할 수 있는 던전 
던전을 최대한 많이 탐험
k : 현재 피로도 
dungeons: 최소필요 피로도, 소모 피로도가 담긴 2차원 배열
return : 탐험할 수 있는 최대 던전수 
"""
# 백트래킹을 진행할 dfs함수 선언: 
# 매개변수 : 현재 피로도 now_fatigue 
#            현재까지 다녀간 던전 수 completed_dungeons
def dfs(now_fatigue, completed_dungeons, visited, dungeons): 
    # max_completed_dungeons_num global로 선언
    global max_completed_dungeons_num 
        
    # 인덱스 i: 0부터 dungeons의 길이 - 1까지 반복하면서
    for i in range(len(dungeons)): 
        # dungeons[i]를 방문하지 않았고 현재 피로도가 dungeons[i][0]보다 같거나 크면 
        if not visited[i] and now_fatigue >= dungeons[i][0]:
            # dungeons[i] 방문 처리
            visited[i] = True 
            # dfs함수 호출 
            dfs(now_fatigue - dungeons[i][1], completed_dungeons + 1, 
                visited, dungeons) 
            # dugeons[i] 미방문 처리 
            visited[i] = False 
            
    # 던전을 다 돌고난 뒤 최대 탐험던전수 큰값 저장
    max_completed_dungeons_num = max(max_completed_dungeons_num, 
                                     completed_dungeons)

def solution(k, dungeons):
    # 최대 던전 탐험 수 max_completed_dungeons_num global로 선언 후 0으로 초기화
    global max_completed_dungeons_num 
    max_completed_dungeons_num = 0 
    # 각 던전들을 방문한적이 있는지 여부 방문테이블 리스트 값은 False로 dugneons길이만큼 초기화 
    visited = [False] * len(dungeons) 
    # dfs 호출 
    dfs(k, 0, visited, dungeons)
    # max_completed_dugneons_num 리턴 
    return max_completed_dungeons_num