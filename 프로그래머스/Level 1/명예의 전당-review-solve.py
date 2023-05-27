"""
상위 k번째 이내 가수 점수를 명예의 전당에 올려 기념
시작이후 초기 k일까지는 모두 명예의 전당에 오름
k일 다음부터 출연 가수점수가 기존 명예 전당 목록 k번째 순위의 가수 점수보다 높으면
출연 가수 점수가 명예의 전당에 오르고 기존 k번째 순위 점수는 명예의 전당에서 내려옴
score: 1일부터 마지막날까지 출연한 가수들의 점수
k: 명예의 전당 목록 점수의 개수 
명예의 전당 최하위 점수를 리턴

우선 순위 큐를 이용하여 k길이가 되면 가장 작은 점수를 리스트에 넣음 
"""
import heapq

def solution(k, score):
    # 최하위 점수를 기록하는 리스트 
    answer = []
    # 명예의 전당 우선순위 큐로 구현 hornors
    hornors = []
    
    # score를 하나씩 탐색하면서 - 원소 i
    for i in score: 
        # 우선순위 큐의 길이가 k보다 작으면 
        if len(hornors) < k:
            # 우선순위큐 hornors에 i 삽입
            heapq.heappush(hornors, i)
        # 우선순위의 큐의 길이가 k이면 
        else:
            # 우선순위 큐 hornors의 첫번째 원소보다 i가 더 크면
            if i > hornors[0]:
                # 우선순위큐 hornors pop
                heapq.heappop(hornors)
                # i를 우선순위큐 hornors에 push
                heapq.heappush(hornors, i)
                
        # 우선순위 큐 hornors에서 가장 작은 원소를 최하위점수 기록 리스트 answer에 append
        answer.append(hornors[0])
        
    return answer