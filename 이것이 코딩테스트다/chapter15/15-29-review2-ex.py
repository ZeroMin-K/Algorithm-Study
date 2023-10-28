import sys
input = sys.stdin.readline
n, c = map(int, input().split())

houses = [] 
for _ in range(n):
    houses.append(int(input()))
    
houses.sort()
result = 0

start = 1
end = houses[-1] - houses[0]

while start <= end: 
    mid = (start + end) // 2
    
    installed_cur = houses[0]
    installed_num = 1
    
    for i in range(1, n):
        if houses[i] >= installed_cur + mid:
            installed_cur = houses[i]
            installed_num += 1
            
    if installed_num >= c:
        start = mid + 1
        result = mid 
    else:
        end = mid - 1 
        
print(result)