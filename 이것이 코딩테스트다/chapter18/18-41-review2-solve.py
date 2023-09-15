"""
n개의 여행지 1~ n번까지 번호로 구분
도로 존재 => 양방향 이동 가능
여행가능한지 여부 

=> 부모가 같으닞 확인 
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
        
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1) 

plan = list(map(int, input().split()))
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        print("NO")
        break
else:
    print("YES")