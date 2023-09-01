"""
n개 집. 0번부터 n - 1번까지 번호로 구분 
M개의 도로. 가로등 구비. 가로등 켜는 비용은 도로 길이와 동일
일부 가로등을 비활성화하여 가로등 켜진 도로만 오가도록
일부 가로등을 비활성화하여 최대한 많은 금액 절약
절약할 수 있는 최대 금액 출력 
모든 집을 방문할 수있으며 가장 비용이 적은 도로만을 만들도록 => MST 이용
모든 가로등 키는 비용 - MST 가로등 비용 
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) 
    return parent[x] 

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
edges = [] 
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))
    edges.append((z, x, y))
    

parent = [i for i in range(n)]
edges.sort() 

total_cost = 0
min_cost = 0
for edge in edges:
    cost, x, y = edge
    total_cost += cost 
    
    if find_parent(parent, x) != find_parent(parent, y):
        union(parent, x, y) 
        min_cost += cost 
        
print(total_cost - min_cost)