"""
모든 음식의 스코빌 지수 k 이상으로 만들기 
스코빌 지수가 가장 낮은 두개음식을 섞음
썩은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + 두번째로 맵지않은 음식의 스코빌 지수 * 2
모든 음식의 스코빌 지수가 k이상될때까지 반복하여 섞기
scovile: 스코빌 지수 담은 배열 
k: 원하는 스코빌 지수 
return : 모든 음식의 스코빌 지수를 k이상으로 만들기 위해 섞어야하는 최소횟수 
K이상으로 만들수없는 경우 -1 리턴 
"""
# heapq import 
import heapq 

def solution(scovilles, k):
    # 섞은 횟수 mix 0으로 초기화 
    mix = 0
    # 힙 q 빈리스트로 초기화 
    q = [] 
    
    # scovilles를 하나씩 탐색하면서 : 원소 scoville
    for scoville in scovilles:
        # q에 scoville을 힙푸쉬
        heapq.heappush(q, scoville)
    
    # q의 길이가 2이상인 동안 반복 진행하면서 
    while len(q) >= 2: 
        # q의 첫번째 원소가 k이상이면
        if q[0] >= k: 
            # 반복 종료
            break 
        
        # q에서 heappop한 음식 스코빌지수 scoville1
        scoville1 = heapq.heappop(q) 
        # q에서 heappop한 음식 스코빌지수 scoville2
        scoville2 = heapq.heappop(q) 
        # scoville1, 2를 섞어서 q에 heappush
        heapq.heappush(q, scoville1 + scoville2 * 2) 
        # mix 1증가
        mix += 1
        
    # q의 첫번째 원소가 k보다 작으면
    if q[0] < k: 
        # mix -1로 변경
        mix = -1
    
    return mix