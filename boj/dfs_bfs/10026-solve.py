"""
적록색약: 빨간색과 초록색의 차이를 못느낌
n * n 크기의 그리드 
    - 각 칸에 R, G, B중 하나 색칠
    - 그림은 몇개의 구역으로 나뉨
    - 구역은 같은 색
    - 같은 색상이 상, 하, 좌, 우로 인접해있는 경우 두 글자는 같은 구역에 속함
    - 색상 차이를 거의 느끼지 못하는 경우도 같은 색상 
적록색약이 아닌 사람이 봤을 때 구역의 개수와 적록색약인 사람이 봤을 때 구역의 수 출력 

적록색약이 아닌 사람이 봤을 때 구역 개수   
    => BFS를 통해서 같은 글자끼리 구역의 개수를 셈
적록색약: R, G를 같은 글자로 취급하며 탐색
    => R, G부분을 같은 글자로 변경 후 BFS를 통해서 같은 글자끼리 구역의 개수 셈 
"""
# 크기 n 입력 
n = int(input()) 
# 적록 색약이 아닌 사람의 색 정보를 저장하는 그리드 norm_graph 빈리스트로 초기화
norm_graph = [] 
# 적록색약인 사람의 색 정보를 저장하는 그리드 rg_graph 빈리스트로 초기화
rg_graph = []
# n번 반복하면서 
for _ in range(n): 
    # 한 줄을 입력받아 data로 초기화
    data = input() 
    # norm_graph에 data를 리스트로 변환 후 삽입
    norm_graph.append(list(data)) 
    # rg_graph에 data에서 R를 G로 변경하여 리스트로 변환 후 삽입
    rg_graph.append(list(data.replace('R', 'G'))) 

# 상, 하, 좌, 우 좌표 값 moves 초기화 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# deque import 
from collections import deque 
# bfs 함수 선언: 매개변수 graph, visited, a, b
def bfs(graph, visited, a, b):
    # deque 생성하여 q로 초기화
    q = deque() 
    # q에 (a, b) 삽입
    q.append((a, b)) 
    # visited[a][b] True로 초기화 
    visited[a][b] = True 

    # q가 빌 때까지 반복
    while q: 
        # x, y는 q에서 popleft한 값
        x, y = q.popleft() 

        # moves를 하나씩 탐색하면서 : 원소 move 
        for move in moves: 
            # nx, ny는 x + move[0], y + move[1]
            nx, ny = x + move[0], y + move[1] 
            
            # nx, ny과 0보다 작거나 n보다 같거나 크면
            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                # continue
                continue 

            # graph[x][y]와 graph[nx][ny]가 같고 visited[nx][ny]가 False이면 (방문한적 없으면)
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]: 
                # visited[nx][ny]는 True로 변경 (방문 처리) 
                visited[nx][ny] = True 
                # q에 (nx, ny) 삽입 
                q.append((nx, ny)) 

# 적록색약이 아닌 사람이 봤을 때 구역 개수 norm_areas 0으로 초기화 
norm_areas = 0
# 방문테이블 norm_visited 값은 False로 n * n 크기로 초기화 
norm_visited = [[False] * n for _ in range(n)]
# 적록색약인 사람이 봤을 때 구역 개수 rg_areas 0으로 초기화
rg_areas = 0 
# 방문테이블 rg_visited 값은 False로 n * n 크기로 초기화 
rg_visited = [[False] * n for _ in range(n)] 

# 그래프, 방문테이블, 구역 개수를 원소로하는 리스트 cases
cases = [[norm_graph, norm_visited, norm_areas], [rg_graph, rg_visited, rg_areas]]

for k in range(len(cases)): 
    graph, visited, areas = cases[k] 

    # 인덱스 i: 0부터 n - 1까지 반복하면서  
    for i in range(n): 
        # 인덱스 j: 0부터 n - 1까지 반복하면서 
        for j in range(n): 
            # visited[i][j]가 False 이면 
            if not visited[i][j]: 
                # areas 1 증가
                areas += 1
                # bfs 호출: 인자 graph, visited, i, j
                bfs(graph, visited, i, j)

    cases[k][2] = areas 

# cases[0][2], cases[1][2] 출력
print(cases[0][2], cases[1][2])