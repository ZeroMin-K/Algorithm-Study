"""
n개의 송전탑. 전선을 통해 하나의 트리 형태로 연결
하나를 끊어서 2개로 분할 => 두 전력망이 갖게되는 송전탑의 개수를 최대한 비슷하게 맞춤
n : 송전탑 개수 
wires: 전선 정보 
return : 전선 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나눌때
    두 전력망이 가지고 있는 송전탑의 개수 차이 
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

def solution(n, wires):
    # 송전탑의 최소 개수 차이 min_diff n으로 저장 
    min_diff = n 
    # 인덱스 k: 0부터 n - 2까지 반복 진행 
    for k in range(n - 1): 
        # << k번째 전선 제외하고 나머지 연결진행 >>
        # 송전탑의 번호들을 저장하는 부모 테이블 parents 자기자신으로 하여 길이 n + 1 리스트 생성
        parents = [i for i in range(n + 1)]
        # 인덱스 i: 0부터 n - 2까지 반복 진행
        for i in range(n - 1): 
            # i와 k가 다를 때
            if i != k: 
                # wires[i][0]과 wires[i][1] union 
                union_parent(parents, wires[i][0], wires[i][1])
                
        # << 분할된 네트워크에서 송전탑 개수 세기 >> 
        # 분할된 네트워크 개수 세기 
        networks = [0] * (n + 1)
        for i in range(1, n + 1):
            networks[find_parent(parents, i)] += 1
        
        # 분할된 네트워크의 루트 네트워크 리스트 생성
        roots = [i for i in range(1, n + 1) if networks[i] > 0]
        
        # 루트 네트워크가 2개가 아니면 제외 
        if len(roots) != 2:
            continue
            
        # 두 개의 네트워크 송전탑 개수 차이 비교 
        min_diff = min(abs(networks[roots[0]] - networks[roots[1]]), min_diff)
    
    return min_diff