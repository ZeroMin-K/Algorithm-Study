from itertools import combinations

data = [int(input()) for _ in range(9)]

for one_combi in combinations(data, 7):
    if sum(one_combi) == 100:
        for height in sorted(one_combi):
            print(height)
        break