"""
n개의 여행지. 1~ n번까지 번호로 구분
여행지 사이 도로 존재 
여행지가 도로로 연결되면 양방향으로 이동 가능 
하나의 여행 게획을 세운뒤 여행 계획이 가능한지 여부 판단
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

# 여행지 수 n, 여행 계획에 속한 도시수 m 입력
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
# n번반복하면서 
for i in range(n):
    # 여행지가 서로 연결되어있는 여부 주어짐. 1 : 연결, 0 : 미연결
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)
            
# 여행계획에 포함된 여행지 번호 입력 
plan = list(map(int, input().split()))

result = True 
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent[i + 1]):
        result = False 

# 여행계획이 가능하면 YES, 불가능하다면 NO 출력 
if result:
    print('YES')
else:
    print("NO")