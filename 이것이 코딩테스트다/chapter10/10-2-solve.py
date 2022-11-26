"""
학생들에게  0번부터 n번까지 번호 부여 - 처음에 서로다른팀으로 구분
N + 1개팀 존재 
팀합치기 - 두팀을 합침
    - 0 a b : a번 학생이 속한팀과 b번 학생이 속한팀을 합침 
같은 팀여부확인 - 두 학생이 같은팀에 속하는지 확인
    - 1 a b: a번 학생과 b번 학생이 같은팀에 속하는지 확인 
m개의 연산 수행시
같은 팀 여부확인 연산에 대한 연산결과 출력

union, find 문제 
"""

# find_parent 함수 - parent, x
def find_parent(parent, x):
    # x에 대한 parent가 x가 아니면
    if parent[x] != x:
        # parent[x]에 대한  find_parent
        parent[x] = find_parent(parent, parent[x])
    # parent[x] 리턴 
    return parent[x]

# union함수 - parent, a, b
def union(parent, a, b):
    # a: find_parent
    a = find_parent(parent, a)
    # b: find_parent
    b = find_parent(parent, b)
    # a가 더크면 
    if a > b:
        # a의 parent가 b
        parent[a] = b
    # b가 더크면
    else: 
        # b의 parent가 a
        parent[b] = a

# n(학생수 번호 ), m(연산개수) 입력
n, m = map(int, input().split())

# 부모테이블 생성
parent = [0] * (n + 1)

# 부모 테이블 자기자신으로 부모 초기화
for i in range(n+1):
    parent[i] = i

# m번 반복하며 연산입력
for _ in range(m):
    # 연산, a, b 입력 
    op, a, b = map(int, input().split())
    # 연산이 0이면 - 팀합치기 => union
    if op == 0:
        union(parent, a, b)
    # 연산이 1이면 - 같은팀 여부 확인 => find_parent
    else:
        # a의 parent찾기
        a  = find_parent(parent, a)
        # b의 parent찾기
        b = find_parent(parent, b)
        # 둘이 같으면
        if a == b:
            # YES
            print('YES')
        # 다르면
        else:
            # NO
            print('NO')

