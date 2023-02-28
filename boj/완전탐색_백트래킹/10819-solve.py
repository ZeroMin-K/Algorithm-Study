from itertools import permutations 

n = int(input())
data = list(map(int, input().split()))

result = 0
for case in list(permutations(data, n)):
    temp = 0
    for i in range(len(case) - 1):
        temp += abs(case[i] - case[i + 1])

    result = max(result, temp)

print(result)