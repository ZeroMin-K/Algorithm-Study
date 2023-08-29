from itertools import combinations

n, m = map(int, input().split())
chickens, houses = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            houses.append((i, j))
        elif data[j] == 2:
            chickens.append((i, j))
            
candidates = list(combinations(chickens, m))

def get_sum(candidate):
    result = 0 
    for hx, hy in houses:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
        
    return result 

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
            
print(result)