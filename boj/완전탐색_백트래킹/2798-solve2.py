# 카드 개수 n, m 입력
n, m = map(int, input().split())
# 카드 리스트 입력 
cards = list(map(int, input().split()))


visited = [False] * n 

result = 0
def dfs(count, current):
    global result 
    
    if current > m or count > 3:
        return 

    if count == 3:
        if current <= m and abs(m - current) < abs(m - result):
            result = current
        return 
    
    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            dfs(count + 1, current + cards[i])
            visited[i] = False


# m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합 출력
dfs(0, 0)

print(result)