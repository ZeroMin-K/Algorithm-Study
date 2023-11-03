"""
도시 n개. 임의의 두 도시 길이 있을수도 없을수도있음
여행일정이 주어졌을때 여행 경로가능한지 
여행 가능한지 여부 판별

같은 도시 여러 방문 가능 

"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] 

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 도시 수 n 입력
n = int(input()) 
# 여행 계획에 속한 도시수 m 입력
m = int(input()) 

parent = [i for i in range(n + 1)]

# n번 반복하면서
for i in range(1, n + 1): 
    # 연결정보 입력. i번째 줄 j번째 수는 i번 도시 j번도시 연결정보. 
    data = list(map(int, input().split()))
    
    for j in range(n): 
        if data[j] == 1:
            union_parent(parent, i, j + 1)
            
# 여행 계획 입력 
plans = list(map(int, input().split()))

can_travel = True
for i in range(1, m):
    if find_parent(parent, plans[i - 1]) != find_parent(parent, plans[i]):
        can_travel = False 
    
# 가능하면 YES, 불가능하면 NO 출력 
print('YES' if can_travel else 'NO')