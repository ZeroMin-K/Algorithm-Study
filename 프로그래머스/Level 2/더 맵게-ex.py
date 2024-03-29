import heapq 

def solution(scoville, K):
    heapq.heapify(scoville) 
    answer = 0
    while True: 
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return - 1
        second = heapq.heappop(scoville) 
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    
    return answer