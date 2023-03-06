"""
양의 정수 카드 리스트. n장 카드를 모두 숫자가 보임
딜러가 숫자m 외침. 플레이어는 제한된 시간안에 n장 카드중 3장 카드 고르기
n장 카드 => m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합 출력

"""

# 카드 개수 n, m 입력
n, m = map(int, input().split())
# 카드 리스트 입력 
cards = list(map(int, input().split()))


from itertools import combinations 

result = 0
# 3개수 뽑는 조합리스트 하나씩 탐색하며
for combi in list(combinations(cards, 3)):
    now = sum(combi) 
    # 3개의 합이 M을 넘지 않으면서 
    # 이전의 수 리스트의 합에서 m뺐을 때 절대값과 현재 3개 합에서 m뺏을때 절대값 중 지금이 더 작으면
    if now <= m and abs(m - now) < abs(m - result): 
            # 지금 수를 저장 
            result = now 

# m을 넘지 않으면서 m에 최대한 가까운 카드 3장 합 출력
print(result)