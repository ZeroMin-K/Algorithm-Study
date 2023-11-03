"""
컴퓨터와 컴퓨터를 모두 연결하는 네트워크 구축 
a와 b가 연결. a에서 b로 경로가 존재 
컴퓨터 연결하는 비용을 최소로
모든 컴퓨터를 연결하는데 필요한 최소 비용
MST를 이용하여 풀이 
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

# 빠른 입력
import sys
input = sys.stdin.readline

# 컴퓨터 수 n 입력
n = int(input()) 
# 연결할 수 있는 선의 수 m 입력
m = int(input())

# 각 간선들을 저장하는 리스트
edges = [] 
# m번 반복하면서
for _ in range(m): 
    # a, b, c 입력
    a, b, c = map(int, input().split())
    # a컴퓨터와 b 컴퓨터를 연결하는데 비용이 c 듬. edges에 추가
    if a != b: 
        edges.append((c, a, b))

edges.sort()

min_cost = 0 
parent = [i for i in range(n + 1)]

for edge in edges:
    c, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += c
        
print(min_cost)