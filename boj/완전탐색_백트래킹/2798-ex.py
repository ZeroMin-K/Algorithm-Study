# 카드 개수 n, m 입력
n, m = map(int, input().split())
# 카드 리스트 입력 
cards = list(map(int, input().split()))

result = 0 
def dfs(selected):
    global result 
    
    if len(selected) == 3:
        if sum(selected) <= m:
            result = max(result, sum(selected))
        return 
    
    for card in cards: 
        if card not in selected:
            selected.append(card)
            dfs(selected)
            selected.pop()

# m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합 출력
dfs([])

print(result)