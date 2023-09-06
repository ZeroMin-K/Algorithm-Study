"""
n * n 크기 땅. 1 * 1개의 칸으로 나뉨
각 땅에는 나라가 하나씩 존재. 
r행 c열에 있는 나라에 A[r][c]명이 살고있음
국경선 존재. 모든 나라 1*1 크기 => 모든 국경선은 정사각형 형태 

인구이동 진행
    - 하루동안 진행. 더이상 아래 방법에 의해 인구이동이 없을 때까지 지속
    - 국경선을 공유하는 두 나라의 인구차이가 L명 이상, R명이하이면 
        두 나라 공유하는 국경선을 오늘 하루동안 염
    - 국경선이 모두 열리면 인구 이동 시작 
    - 국경선이 열려있어 인접한 칸만을 이용해 이동가능하면 오늘 하루동안은 그나라들 연합
    - 연합을 이루고있는 각 칸 인구수는(연합의 인구수) / (연합을 이루고있는 칸의 개수)
        소수점 버림
    - 연합 해체 후 모든 국경선 닫음

각 나라 인구수가 주어졌을대 인구이동이 며칠동안 발생하는지 구함 

각 나라들을 상, 하, 좌우로 확인하면서 L명이상 R명이하면 인구이동진행
l명 이상 r명 이하인 나라가 다 탐색해도 없으면 인구이동 끝 출력 

"""

# n, l, r 입력
n, l, r = map(int, input().split())
# 각 나라들의 인구수를 저장하는 2차원 리스트 countries 빈리스트로 초기화 
countries = []
# n번 반복하면서
for _ in range(n): 
    # 각 나라 인구수 주어짐 countries에 입력 삽입 
    countries.append(list(map(int, input().split())))

# 상, 하, 좌, 우로 움직이는 리스트 moves
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# deque import
from collections import deque 
# bfs를 진행하는 unite 함수 선언 : 매개변수 visited, start_x, start_y 
def unite(visited, start_x, start_y): 
    # q를 deque로 선언 
    q = deque() 
    # q에 start_x, start_y 삽입
    q.append((start_x, start_y))
    # start_x, start_y 방문 처리
    visited[start_x][start_y] = True  
    # 현재 연합을 이루는 나라들을 리스트  united_countries 빈 리스트로 초기화 
    united_countries = [] 
    # united_countries에 (start_x, start_y 삽입 )
    united_countries.append((start_x, start_y))
    # 현재 연합을 했는지 여부 is_united False로 초기화 
    is_united = False 

    # q가 빌 때까지 반복 
    while q: 
        # x, y는 q에서 popleft한 값
        x, y = q.popleft() 
        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves: 
            # nx는 x + move[0]
            nx = x + move[0] 
            # ny는 y + move[1]
            ny = y + move[1]

            # nx가 0보다 작거나 nx가 n보다 같거나 크거나 ny가 0보다 작거나 ny가 n보다 같거나 크면
            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                # continue
                continue 

            # 방문한적이 없고 countries[nx][ny] - countries[x][y]가 l이상 r이하이면 
            if not visited[nx][ny] and l <= abs(countries[nx][ny] - countries[x][y]) <= r: 
                # 큐에 (nx, ny) 추가
                q.append((nx, ny)) 
                # united_countries에 (nx, ny) 삽입 
                united_countries.append((nx, ny)) 
                # [nx][ny] 방문 처리 
                visited[nx][ny] = True 
                # is_uninted True로 변경 
                is_united = True 

    # is_united_가 False이면 
    if not is_united: 
        # is_united 리턴 
        return is_united 

    # 현재 연합의 인구수 united_people 0으로 초기화 
    united_people = 0 
    # united_countries를 하나씩 탐색하면서 : 원소 x, y
    for x, y in united_countries: 
        # united_people 에 countries[x][y]값 더함
        united_people += countries[x][y] 

    # 연합 인수 수 people 는 united_people / united_countries 길이
    people = int(united_people / len(united_countries))
    # united_countries를 하나씩 탐색하면서 : 원소 x, y 
    for x, y in united_countries: 
        # countries[x][y]의 값은 people 로 값 변경 
        countries[x][y] = people 

    # is_united 리턴 
    return is_united 

# 인구 이동 발생한 날짜 days 0을 초기화 
days = 0 
# 인구 이동이 가능한지 여부 can Move True로 초기화
can_move = True 
# canMove가 True인 동안 반복 진행 (인구 이동이 가능한 동안 반복 진행)
while can_move: 
    # canMove를 False로 초기화 (현재 상태에서 인구이동이 불가능한 상태로 판단)
    can_move = False 
    # 각 나라들을 방문했는지 방문 테이블 visited [False]로 n * n 크기로 초기화 
    visited = [[False] * n for _ in range(n)]
    # 인덱스 i: 0부터 n - 1까지 반복하면서 
    for i in range(n): 
        # 인덱스 j: 0부터 n - 1까지 반복하면서 
        for j in range(n): 
            # 현재 나라 countries[i][j] 
            # unite가 true이면 (unite 호출 인자 visited, i, j)
            if unite(visited, i, j): 
                # canMove True로 초기화 
                can_move = True 

    # canMove가 True이면
    if can_move: 
        # days 1 증가 
        days += 1

# 인구이동이 며칠동안 발생하는지 출력 
print(days) 
