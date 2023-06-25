# 지도 세로 크기 n, 가로크기 m 입력
n, m = map(int, input().split())
# 연구소 labs 빈리스트로 초기화 
labs = [] 
# 바이러스 위치 좌표를 저장하는 viruses 빈리스트로 초기화 
viruses = [] 
# 벽을 세울 수 있는 빈공간 리스트 blanks 빈리스트로 초괴화
blanks = [] 
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
        elif data[j] == 0:
            blanks.append((i, j))
    
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
    
# 안전영역 최대갯수 max_safe 0으로 초기화                
max_safe = 0

from itertools import combinations 
for combi_case in list(combinations(blanks, 3)):
    copied_labs = copy.deepcopy(labs) 
    for case in combi_case:
        copied_labs[case[0]][case[1]] = 1 
        
    # viruses를 하나씩 탐색하면서 - 원소 virus
    for virus in viruses: 
        # spread_virus 호출. 인자 labs, 현재 바이러스 좌표 virus[0], virus[1] 
        spread_virus(copied_labs, virus[0], virus[1])
    
    # max_safe는 max_safe와 count_safe를 호출해서 리턴한 값중 최댓값
    max_safe = max(max_safe, count_safe(copied_labs))

# max_safe 출력 
print(max_safe)