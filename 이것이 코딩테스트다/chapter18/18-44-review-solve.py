"""
n개의 행성. 행성을 연결하는 터널
3차원 좌표위 한점
연결 비용 min(|xa - xb|, |ya - yb|, |za - zb|)
터널 n - 1개를 건설해 모든 행성이 서로 연결되도록 함
모든 행성을 터널로 연결하는데 필요한 최소 비용 구하기 
"""
import sys
input = sys.stdin.readline

# x의 parent를 찾아서 반환 함수 find_parent : 매개변수 parent, x 
def find_parent(parent, x): 
    # x와 parent[x]가 다르면
    if x != parent[x]:
        # parent는 find_parent(parent, parent[x]) 
        parent[x] = find_parent(parent, parent[x]) 
    # parent[x] 리턴
    return parent[x] 

# a, b 를 합치는 함수 union : 매개변수 parent, a, b
def union_parent(parent, a, b):
    # a의 부모 찾음
    a = find_parent(parent, a)
    # b의 부모 찾음
    b = find_parent(parent, b) 
    # a가 b보다 작으면
    if a < b: 
        # b의 부모는 a
        parent[b] = a
    # 나머지
    else: 
        # a의 부모는 b
        parent[a] = b

# 행성 개수 n 입력
n = int(input()) 
# x좌표 리스트
xs = []
# y좌표 리스트
ys = [] 
# z좌표 리스트 
zs = [] 
# 인덱스 i: 1부터 n번 반복하면서
for i in range(1, n + 1): 
    x, y, z = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i)) 

xs.sort()
ys.sort()
zs.sort() 

# 최소 비용 min_cost 
min_cost = 0
# 모든 간선 edges 
edges = [] 
# 부모테이블 n + 1 길이로 자기 자신으로 초기화 
parent = [i for i in range(n + 1)]

for i in range(n - 1): 
    edges.append((xs[i + 1][0] - xs[i][0], xs[i][1], xs[i + 1][1]))
    edges.append((ys[i + 1][0] - ys[i][0], ys[i][1], ys[i + 1][1]))
    edges.append((zs[i + 1][0] - zs[i][0], zs[i][1], zs[i + 1][1]))

edges.sort()
for edge in edges: 
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost

# min_cost 출력 
print(min_cost)