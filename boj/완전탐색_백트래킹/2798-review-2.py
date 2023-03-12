"""
n장 카드 m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합 구해 출력 
백트래킹을 이용해 풀이 
현재 카드 리스트가 3장이고 m을 넘지 않으면서 m에 최대한 가까운지 dfs를 통해서 확인하면서 진행 
"""

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합 결과 저장 
result = 0
# dfs 선언 - 매개변수 : 리스트
def dfs(current):
    # 결과 global 로 선언 
    global result 
    # 현재 리스트의 길이가 3보다 크거나 리스트합이 m보다 크면 
    if len(current) > 3 or sum(current) > m:
        # return 
        return 
    
    # 현재 리스트의 길이가 3이고 리스트합이 m보다 작으면
    if len(current) == 3 and sum(current) <= m:
        # 현재 결과값과 현재 리스트의 합 비교 해서 더 큰쪽 비교 
        result = max(result, sum(current))
        return 
        
    # 카드 리스트 하나씩 반복하면서
    for card in cards:
        # 현재 카드를 방문 안했으면
        if card not in current:
            # 방문처리하고 
            current.append(card)
            # dfs 진행
            dfs(current)
            # 다시 방문 안한 처리 
            current.pop()

# 백트래킹 진행 
dfs([])

# 결과 변수 print 
print(result)