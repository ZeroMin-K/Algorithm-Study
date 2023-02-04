data = list(map(int, input().split()))

answer = sum([num ** 2 for num in data]) % 10 

print(answer)