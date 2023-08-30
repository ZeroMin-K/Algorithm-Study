"""
n * n 크기 복도. 1 * 1 크기 로 나뉨. 특정 위치 선생, 학생, 장애물 위치
각 선생은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시
복도에 장애물이 위치한 경우 선생은 장애물 뒤편 숨은 학생 못봄
상, 하, 좌우 4가지 방향에 대해 장애물로 막히기 전가지 모든 학생 볼 수 잇음
장애물을 정확히 3개 설치하여 모든 학생들이 감시로 피할 수 있는지 출력 
"""

# 자연수 n
n = int(input()) 
# 복도에 대한 2차원 리스트 graph 빈리스트로 초기화 
graph = [] 
# 선생의 위치 teachers 빈리스트로 초기화 
teachers = [] 
# 장애물을 설치할 수 있는 빈칸 위치 blanks 빈 리스트로 초기화 
blanks = [] 
# 인덱스 i: 0부터 n - 1까지 반복하면서 
for i in range(n): 
    # 복도 정보 data 공백구분으로 리스트로 입력. (학생 : S, 선생 : T, 없음 : X)
    data = list(input().split())
    # 인덱스 j: 0부터 n - 1까지 반복하면서 
    for j in range(n): 
        # data[j]가 T이면 
        if data[j] == 'T':
            # teachers에 (i, j) 삽입
            teachers.append((i, j)) 
        # data[j]가 X이면
        elif data[j] == 'X': 
            # blanks에 (i, j) 삽입 
            blanks.append((i, j)) 
    # graph에 data 삽입 
    graph.append(data) 

# 상, 하, 좌, 우 4가지 방향에 대한 리스트 fowards
forwards = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# tx, ty에서 선생이 감시를 진행 watch 
def watch(tx, ty):  
    # 학생을 못 찾았는지 여부 not_found True로 초기화 
    not_found = True 
    # 상, 하, 좌우 4가지 방향을 확인하면서 원소 dx, dy
    for dx, dy in forwards: 
        # 다음 위치 nx, ny는 tx + dx, ty + dy 
        nx, ny = tx + dx, ty + dy 
        # nx, ny가 0보다 같거나 크거나 n보다 작은 동안 반복진행 
        while 0 <= nx < n and 0 <= ny < n: 
            # graph[nx][ny]가 'O'이면 (장애물) 
            if graph[nx][ny] == 'O':
                # 반복 종료 
                break
            # graph[nx][ny]가 'S'이면 (학생발견)
            elif graph[nx][ny] == 'S':
                # not_found False로 초기화 
                not_found = False 
                break 
            # nx, ny는 nx + dx, ny + dy 
            nx, ny = nx + dx, ny + dy 

    # not_found 리턴
    return not_found 

# 모든 학생이 감시를 피할수 있는 여부 all_passed False로 초기화 
all_passed = False 
# import combinations
from itertools import combinations 
# blanks에서 3개를 뽑는 combinations를 하나씩 탐색하면서 : 원소 combi_case
for combi_case in combinations(blanks, 3): 
    # combi_case를 하나씩 탐색하면서 원소 bx, by 
    for bx, by in combi_case: 
        # graph[bx][by]을 O로 초기화 
        graph[bx][by] = 'O'
    
    # 현재 케이스에서 학생이 감시 피할수있는 여부 passed True로 초기화 
    passed = True 

    # teachers를 하나씩 탐색하면서 : 원소 tx, ty 
    for tx, ty in teachers: 
        # tx, ty부터 탐색시작 (watch 호출) 학생이 감시를 못 피하면 
        if not watch(tx, ty): 
            passed = False 

    # passed가 True이면 all_passed True로 변경
    if passed:
        all_passed = True 

    # graph[bx][by]을 X로 초기화 
    for bx, by in combi_case: 
        graph[bx][by] = 'X' 

# 모든 학생이 감시로 피할 수 있으면 all_passed가 True이면
if all_passed: 
    # YES 출력
    print('YES')
# 피할 수 없다면 
else: 
    # NO 출력
    print("NO")