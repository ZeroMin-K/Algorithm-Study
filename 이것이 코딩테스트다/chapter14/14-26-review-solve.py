"""
카드 수 a, b인 두 묶음의 정렬된 숫자카드
하나로 합치는데 a + b번 비교
n개의 숫자 카드 묶음이 각각 크기 주어질때 최소한 몇번의 비교가 필요한지 출력
가장 작은 카드 묶음끼리 합쳐서 비교숫자 구하기

힙을 이용하여 두 개의 카드 묶음을 뽑고 합친다음 다시 힙에 넣음
힙에 1개가 남을때 최종 비교횟수

"""

import sys
input = sys.stdin.readline 

# 카드 묶음 수 n입력
n = int(input())
# 카드 묶음 리스트 cards 빈리스트로 초기화 
cards = [] 
# heapq import 
import heapq 
# n번 반복하면서 
for _ in range(n): 
    # 각 카드 묶음의 카드 개수 입력하여 카드 묶음 리스트 cards에 heappush 
    heapq.heappush(cards, int(input()))

# 총 비교횟수 
count = 0
# 힙큐의 길이가 2개 이상인동안
while len(cards) >= 2: 
    # 비교할 숫자카드 묶음의 카드 수 a 힙큐에서 pop
    a = heapq.heappop(cards)
    # 비교할 숫자카드 묶음의 카드 수 b 힙큐에서 pop
    b = heapq.heappop(cards)
    # 총 비교횟수에 a + b를 더함
    count += a + b
    # a + b의 카드 묶음을 다시 힙큐에 push
    heapq.heappush(cards, a + b) 

# 힙큐에서 pop에서 출력 
print(count)