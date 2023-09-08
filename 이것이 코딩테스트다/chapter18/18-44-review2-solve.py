"""
n개의 행성 
연결하려는 행성 만듬
두 행성간 비용은 min(|xa - xb|, |ya - yb|, |za - zb|)
터널을 총 n- 1개 건설해서 모든 행성이 서로 연결되게 하려고 함
모든 행성을 터널로 연결하는데 필요한 최소 비용 구하기 

MST를 이용한 방법 
"""
import sys
input = sys.stdin.readline

# find_parent 함수: 매개변수 parent, x
def find_parent(parent, x):
    # parent[x]가 x와 다르면
    if parent[x] != x: 
        # parent[x]는 find_parent
        parent[x] = find_parent(parent, parent[x]) 
    # parent[x] 리턴 
    return parent[x] 
    
# union_parent함수: 매개변수 parent, a, b
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

xs = []
ys = [] 
zs = [] 

# 행성의 개수 n 입력
n = int(input()) 
# 인덱스 i: 0부터 n - 1번 반복하면서 
for i in range(n): 
    # x, y, z 좌표 주어짐
    x, y, z = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))
    
    
xs.sort()
ys.sort()
zs.sort()
    
edges = [] 
for i in range(1, n):
    # 비용, i, i - 1
    edges.append((xs[i][0] - xs[i - 1][0], xs[i][1], xs[i - 1][1]))
    edges.append((ys[i][0] - ys[i - 1][0], ys[i][1], ys[i - 1][1]))
    edges.append((zs[i][0] - zs[i - 1][0], zs[i][1], zs[i - 1][1]))
    
# 간선 edges들을 모두 정렬
edges.sort() 
# 각 원소들에 대해 부모들을 자기 자신으로 초기화 
parent = [i for i in range(n)]

# 최소 비용 min_cost = 0으로 초기화 
min_cost = 0 
# edges를 하나씩 탐색하면서 : 원소 edge
for edge in edges:
    cost, a, b = edge
    # a의 부모를 찾고, b의 부모를 찾아서 서로 다르면    
    if find_parent(parent, a) != find_parent(parent, b):
        # a, b union_parent
        union_parent(parent, a, b) 
        # 비용을 min_cost에 더함 
        min_cost += cost 
        
# min_cost 출력 
print(min_cost)