"""
매일 1명의 가수 노래, 문자 투표수로 점수부여
매일 출연한 가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 명예전당 목록에 올림

프로그램 초기에 k일까지 모든 출연 가수점수가 명예의 전당 오름
k일 부터 출연 가수 점수가 기존 명예전당목록 k번째 순위의 가수 점수보다 높으면 교체. 

명예전당의 최하위 점수를 발표 
명예 전당 목록 점수의 개수 k, 1일부터 마지막 날까지 출연 가수 점수 score
매일 발표된 명예 전당 최하위 점수 return 

명예전당 리스트 따로 만들어서
하나씩 score탐색하면서  명예 전당리스트 3개 유지하면서 가장 최하위 점수 결과 리스트에 붙여서 출력 
"""

import heapq 

def solution(k, score):
    # 최하위 점수를 기록하는 리스트 
    answer = []
    
    # 명예 전당 리스트 honors (힙큐 구현) - 항상 작은것이 나와야하니 최소힙으로 구현 
    honors = [] 
    
    # score를 하나씩 탐색하면서 - 현재 점수 now 
    for now in score: 
        # 명예 전당 리스트의 길이가 k이하이면
        if len(honors) < k: 
            # 현재 점수 now를 명예 전당 리스트 honors에 push 
            heapq.heappush(honors, now)
        # 명예 전당 리스트의 길이가 k보다 크면
        else:
            # 현재 점수 now와 명예전당 리스트 가장 최소원소비교해서 now가 더크면
            if now > honors[0]: 
                # honors에서 pop
                heapq.heappop(honors)
                # 현재 점수 push 
                heapq.heappush(honors, now)
                        
        # honors의 최솟값(0번재 인덱스) 을 answer에 append
        answer.append(honors[0])
    
    
    return answer