"""
연구소 n * m 직사각형 - 빈칸, 벽으로 이루어짐. 벽은 칸 하나 차지
일부 칸 바이러스 존재, 바이러스는 상, 하, 좌, 우로 인접한 빈칸 모두 퍼져나감
세울 수 있는 벽 개수 3개. 무조건 3개 세움
0 : 빈칸, 1: 벽, 2: 바이러스있는곳. 

바이러스 퍼질 수 없는 안전영역 크기의 최댓값 계산하기

벽을 세개 세운 후 바이러스 퍼뜨리고 안전영역 세우기
벽을 3개 세우는 것은 백트래킹을 이용하고 
바이러스 퍼뜨리는 것을 BFS를 이용하여 풀이
안전영역은 전부다 확인해보기. 
"""

# 지도 세로 크기 n, 가로크기 m 입력
n, m = map(int, input().split())
# 연구소 labs 빈리스트로 초기화 
labs = [] 
# 바이러스 위치 좌표를 저장하는 viruses 빈리스트로 초기화 
viruses = [] 
# 인덱스 i: 0부터 n - 1까지 반복하면서 
for i in range(n):
    # 지도 한 줄씩 공백구분으로 int로 map하여 리스트 data로 만든 후 labs에 append
    data = list(map(int, input().split()))
    labs.append(data)
    # 인덱스 j: 0부터 m - 1까지 반복하면서
    for j in range(m):
        # data[j]가 2이면
        if data[j] == 2: 
            # (i, j)를 viruses에 append
            viruses.append((i, j))
    
# 안전영역을 세는 메서드 count_safe 선언 - 매개변수 labs 
def count_safe(labs):
    # 안전 영역의 개수 safe_nums 0으로 초기화 
    safe_nums = 0
    # 인덱스 i : 0부터 n - 1까지 반복하면서
    for i in range(n):
        # 인덱스 j: 0부터 m - 1까지 반복하면서
        for j in range(m):
            # labs[i][j] 가 0이면
            if labs[i][j] == 0:
                # safe_nums 값 1증가
                safe_nums += 1
                
    # safe_nums 리턴 
    return safe_nums 
    
# deque import 
from collections import deque 
# 바이러스가 상, 하, 좌, 우로 퍼지는 이동 리스트 moves 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1) ]
# 바이러스를 bfs로 퍼뜨리는 메서드 spread_virus 선언 - 매개변수 labs, 현재 바이러스 x, y좌표
def spread_virus(labs, x, y):
    # 큐 q deque로 생성
    q = deque() 
    # 큐에 현재 바이러스 위치좌표 (x, y) append
    q.append((x, y)) 
    
    # 큐가 빌 때까지 반복하는 동안
    while q:
        # 큐에서 popleft하여 현재 좌표 now_x, now_y에 저장
        now_x, now_y = q.popleft() 
        # moves를 하나씩 탐색하면서 - 원소 move 
        for move in moves: 
            # x의 다음 좌표 next_x는 now_x 에 move[0]을 더함
            next_x = now_x + move[0] 
            # y의 다음 좌표 next_y는 now_y에 move[1]을 더함 
            next_y = now_y + move[1] 
            
            # next_x가 0보다 같거나 크고 n보다 작고, next_y가 0보다 같거나 크고 m보다 작으면
            if 0 <= next_x < n and 0 <= next_y < m: 
                # labs[next_x][next_y]가 0이면
                if labs[next_x][next_y] == 0:
                    # labs[next_x][next_y]는 2( 바이러스 퍼짐)
                    labs[next_x][next_y] = 2
                    # 큐에 (next_x, next_y) 삽입
                    q.append((next_x, next_y))
                    
import copy 

# 백트래킹 dfs 선언 - 매개변수 벽의 개수 wall_nums, 연구소 2차원리스트 labs
def dfs(wall_nums, labs):
    # 안전 영역 최소 개수 max_safe global로 선언 
    global max_safe 
    
    if wall_nums > 3:
        return 
    
    # wall_nums가 3이면 => 바이러스 확산
    if wall_nums == 3: 
        # 현재 연구소를 deep copy
        copied_labs = copy.deepcopy(labs) 
        
        # viruses를 하나씩 탐색하면서 - 원소 virus
        for virus in viruses: 
            # spread_virus 호출. 인자 labs, 현재 바이러스 좌표 virus[0], virus[1] 
            spread_virus(copied_labs, virus[0], virus[1])
            
        # max_safe는 max_safe와 count_safe를 호출해서 리턴한 값중 최댓값
        max_safe = max(max_safe, count_safe(copied_labs))
        # 리턴
        return 
    
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n):
        # 인덱스 j: 0부터 m - 1까지 반복하면서
        for j in range(m):
            # labs[i][j]가 0이면
            if labs[i][j] == 0:
                # labs[i][j]는 1로 변경 (벽 설치)
                labs[i][j] = 1
                # dfs 호출 - 인자 wall_nums + 1, labs
                dfs(wall_nums + 1, labs) 
                # labs[i][j]는 0으로 변경 (벽 제거)
                labs[i][j] = 0 

# 안전영역 최대갯수 max_safe 0으로 초기화                
max_safe = 0
# dfs 호출 - 인자 labs, 벽의 개수 0
dfs(0, labs) 
# max_safe 출력 
print(max_safe)