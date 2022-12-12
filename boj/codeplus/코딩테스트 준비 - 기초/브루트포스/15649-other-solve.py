# n, m 입력
n, m = map(int, input().split())

result = []

# DFS를 이용하여 백트래킹 진행 
def dfs():
    # 현재 리스트의 길이가 m이면 
    if len(result) == m:
        print(' '.join(map(str, result)))
        return 

    # 1부터 n까지 반복하며 
    for i in range(1, n + 1):
        # 현재 i가 결과 리스트에 없으면 
        if i not in result:
            # 현재 i를 결과 리스트에 삽입 
            result.append(i)
            # DFS 다시 진행
            dfs()
            # 현재 i를 결과 리스트에서 pop
            result.pop()
dfs() 