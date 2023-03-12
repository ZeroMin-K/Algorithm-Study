"""
n장의 카드 중에서 m을 넘지않으면서 m에 최대한 가까운 카드 3장의 합 구해 출력하기
조합 이용하기 + 백트래킹 이용해보기 
"""

# n, m 입력
n, m = map(int, input().split())
# 카드 리스트 입력
cards = list(map(int, input().split()))

# 결과 
result = 0

from itertools import combinations 
# 조합 리스트 중에서 
for combi in list(combinations(cards, 3)):
    now = sum(combi)
    # 현재 조합의 합이 m을 넘지 않으면서 결과보다 크면 
    if now <= m and now > result:
        result = now
            
# 결과 출력 
print(result)