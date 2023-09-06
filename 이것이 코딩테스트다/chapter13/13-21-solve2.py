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

    # 현재 연합의 인구수 united_people 초기화 
    united_people = countries[start_x][start_y]

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
                united_people += countries[nx][ny] 
                # [nx][ny] 방문 처리 
                visited[nx][ny] = True 
                # is_uninted True로 변경 
                is_united = True 

    # is_united_가 False이면 
    if not is_united: 
        # is_united 리턴 
        return is_united 

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
            if not visited[i][j] and unite(visited, i, j): 
                # canMove True로 초기화 
                can_move = True 

    # canMove가 True이면
    if can_move: 
        # days 1 증가 
        days += 1

# 인구이동이 며칠동안 발생하는지 출력 
print(days) 