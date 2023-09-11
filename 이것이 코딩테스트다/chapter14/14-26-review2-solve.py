"""
두 묶음 카드 수 a, b
두묶음 합쳐서 하나로 만드는데 a + b번 비교
n개의 숫자 카드 묶음 크기 주어지면 최소한 몇번 비교하는지 
가장 작은 카드 끼리 묶어서 합치기
우선순위큐를 이용해 진행
"""
# 빠른 입력 
import sys
input = sys.stdin.readline
# import heapq
import heapq 

# n입력
n = int(input())
# 카드 묶음 수 리스트 cards 빈리스트로 초기화 
cards = [] 
# n번반복하면서 
for _ in range(n):
    # 카드 묶음 크기 card 주어짐
    card = int(input()) 
    # cards에 card를 heappush 
    heapq.heappush(cards, card) 

# 총 비교횟수 compares 0으로 초기화 
compares = 0 
# cards가 빌때까지 반복
while cards: 
    # 첫번째 카드 묶음 first : cards에서 heappop한 값
    first = heapq.heappop(cards)
    # cards가 비어있으면
    if not cards: 
        # 반복 종료 
        break 
    # 두번째 카드 묶음 second: cards에서 heappop한 값
    second = heapq.heappop(cards) 
    # first와 second를 더한 값 compare
    compare = first + second
    # compare을 cards에 heappush 
    heapq.heappush(cards, compare) 
    # compares에 compare을 더함 
    compares += compare 

# compares 출력
print(compares)