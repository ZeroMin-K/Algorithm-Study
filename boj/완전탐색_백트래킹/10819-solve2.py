# n 입력
n = int(input())

# 배열 정수 - 공백 기준으로 입력
data = list(map(int, input().split()))

visited = [False] * n

answer = 0

def dfs(numbers):
    global answer

    if len(numbers) == n:
        total = 0
        for i in range(n - 1):
            total += abs(numbers[i] - numbers[i + 1])
        answer = max(answer, total)

        return 
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            numbers.append(data[i])
            dfs(numbers)
            visited[i] = False
            numbers.pop()

dfs([])
print(answer)

