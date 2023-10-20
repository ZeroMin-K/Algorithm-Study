"""
그래프가 주어졌을 때 그래프의 최소 스패닝 트리 구하기
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

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = [] 
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

parent = [i for i in range(v + 1)] 

edges.sort()
min_weights = 0 
for edge in edges: 
    weight, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        min_weights += weight 
        union_parent(parent, a, b)

print(min_weights)