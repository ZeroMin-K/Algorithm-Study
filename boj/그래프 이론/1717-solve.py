"""
0부터 n까지의 n + 1개의 집합이 있음 
합집합 연산과 두 원소가 같은 집합에 포함되어있는지 확인하는 연산 수행

"""

# 빠른 입력 
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

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

# n, m 입력 
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

# m번 반복하면서
for _ in range(m): 
    # op, a, b 입력
    op, a, b = map(int, input().split())
    # op가 0이면 합집합연산
    if op == 0:
        union_parent(parent, a, b)
    # op가 1이면 두 원소가 같은 집합에 포함되어있는지 확인
    else: 
        # a, b 가 같은 집합에 포함되어있으면
        if find_parent(parent, a) == find_parent(parent, b): 
            # "YES" 출력
            print("YES") 
        # 그렇지 않으면 
        else: 
            # "NO" 출력 
            print("NO")