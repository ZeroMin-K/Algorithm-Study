"""
두 묶음 숫자 카드 - 카드 수 A, B  
두 묶음을 합쳐서 하나로 만드는데 A + B번 비교 
N개의 숫자 카드 묶음의 각각의 크기가 주어질때 최소한 몇번 비교가 필요한지 
"""
import heapq

# 카드 묶음 수 저장하는 리스트 생성
cards = [] 
# n 입력
n = int(input())
# n개 줄에 걸쳐 숫자 카드 묶음 크기 입력
for _ in range(n):
    heapq.heappush(cards, int(input()))

total_count = 0
while len(cards) != 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

    count = first + second
    total_count += count

    heapq.heappush(cards, count)

print(total_count)