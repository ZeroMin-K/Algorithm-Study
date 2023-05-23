"""
바이러스가 퍼지고 확산 막기위해 연구소에 벽세움
연구소 크기 n * m. 빈칸, 벽으로 이루어져있음
일부 칸 바이러스 존재. 상하좌우 인접한 빈칸으로 모두 퍼짐
벽을 3개만 세울 수 있으며 무조건 3개 세워야함
0: 빈칸, 1: 벽, 2: 바이러스
벽이 없으면 빈칸으로 퍼져나감
바이러스가 퍼질수없는 곳을 안전영역
안전영역 크기의 최댓값 구하는 프로그램 작성하기 

매번 벽을 3개 세우면서 BFS를 통해 바이러스를 퍼뜨리며 안전영역매번세면서 최댓값 찾기 
최대 크기가 8이므로 벽을 세울때 N^3으로 세워도 가능

"""

# 지도 세로크기 n 가로크기 m 입력 
n, m = map(int, input().split())

# 현재 지도 그래프 빈리스트로 초기화
graph = [] 

# 바이러스 위치를 담는 리스트 viruses 빈리스트로 초기화
viruses = [] 
# 벽을 세울 수 있는 빈칸을 담는 리스트 blanks 빈 리스트로 초기화 
blanks = [] 
# n번 반복하면서
for i in range(n):
    # 지도 입력. 공백 구분을 리스트 입력하여 지도에 append
    data = list(map(int, input().split()))
    graph.append(data)
    
    # 현재 한줄을 0부터 m - 1까지 반복하면서 
    for j in range(m):
        # 현재 입력에 2가 있으면(바이러스이면) 
        if data[j] == 2:
            # 바이러스 리스트에 현재 위치 append
            viruses.append((i, j))
        #현재 입력에 0이 있으면 (빈공간이면)
        elif data[j] == 0:
            # 빈공간 리스트에 append
            blanks.append((i, j))
            
# 위아래로 움직일 수 있는 리스트 생성 상, 하, 좌, 우
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

from collections import deque 

# bfs 함수선언 
def bfs(lab, x, y):
    # 현재 시작위치를 deque에 넣음
    q = deque()
    q.append((x, y))
        
    # 큐가 빌때까지
    while q:
        # 현재 위치를 큐에서 빼냄
        now = q.popleft()
        
        # 움직임 리스트를 하나씩 반복하면서
        for move in moves: 
            # 다음 좌표는 움직임리스트에서 움직임
            next_x = now[0] + move[0]
            next_y = now[1] + move[1]
            # 다음 좌표가 지도 인덱스에 맞으면
            if 0 <= next_x < n and 0 <= next_y < m:
                # 다음좌표가 0이면 (현재 빈칸) 
                if lab[next_x][next_y] == 0:
                    # 다음좌표 2로 바꿈(바이러스 퍼짐)
                    lab[next_x][next_y] = 2
                    # 다음 좌표를 큐에 넣음 
                    q.append((next_x, next_y))
                    
# 안전영역 세는 함수선언
def count_safe(graph):
    # 현재 안전영역은 0으로 초기화 
    safe = 0
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n):
        # 인덱스 j: 0부터 m - 1까지 반복하면서
        for j in range(m):
            # 현재 좌표가 0이면
            if graph[i][j] == 0:
                # 안전영역 개수 증가
                safe += 1
    # 안전영역 개수 리턴 
    return safe 

# 안전 영역의 최댓값 0으로 초기화       
max_safe = 0

import copy 
from itertools import combinations 
# 빈공간에 대한 리스트를 combinations으로 3개를 뽑는 경우에 대해 하나씩 반복하면서
for combi_case in list(combinations(blanks, 3)):
    # 벽3개를 만들 새로운 그래프 copy하여 생성 
    lab = copy.deepcopy(graph)
    
    # 현재 빈공간에 경우를 다 벽으로 바꿈
    for wall in combi_case:
        lab[wall[0]][wall[1]] = 1
    
    # 바이러스 리스트를 하나씩 탐색하면서
    for virus in viruses: 
        # 현재 바이러스 위치로부터 BFS 진행
        bfs(lab, virus[0], virus[1])
        
    # 지도를 하나씩 세면서 빈칸개수를 셈
    # 빈칸개수를 저장한 빈칸개수와 비교하며 가장 큰것을 저장
    max_safe = max(max_safe, count_safe(lab))

# 안전 영역 최댓값 출력 
print(max_safe)