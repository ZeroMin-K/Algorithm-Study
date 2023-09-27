"""
어떤 지역높이 정보 확인
많은 비내릴때 물에 잠기지 않는 안전한 영역이 최대로 몇개가 만들어지는지 조사
장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정 
행과열의 크기가 n인 2차원 배열 형태의 높이 정보 
안전영역은 물에 잠기지 않는 지점들이 상, 하, 좌, 우 인접해있으면서 크기가 최대인 영역

현재 위치에서부터 물에 잠기지 않는 영역들을 세면서 최대 안전영역 개수 찾기 
"""

# 빠른 입력 
import sys
input = sys.stdin.readline

# n 입력
n = int(input())
# 각 지역 정보를 저장하는 2차원 리스트 graph 빈 리스트로 초기화 
graph = []
# n번 반복하면서 
for _ in range(n): 
    # 공백구분으로 한 줄 입력받아 graph에 삽입
    graph.append(list(map(int, input().split())))
    
# 최대 안전영역 max_safe 0으로 초기화
max_safe = 0 

# 상, 하, 좌, 우로 움직이는 리스트 moves 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# deque import 
from collections import deque 
# bfs 함수 선언 : 현재 위치 start_x, start_y, height 
def bfs(start_x, start_y, height): 
    # 큐 q deque로 생성
    q = deque() 
    # (start_x, start_y) 삽입 
    q.append((start_x, start_y))
    # (start_x, start_y) 방문 처리 
    visited[start_x][start_y] = True 
    
    # q가 빌 때까지 반복하면서 
    while q: 
        # 현재 위치 x, y는 q에서 popleft한것
        x, y = q.popleft() 
        
        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves: 
            # nx, ny는 x + move[0], y + move[1]
            nx, ny = x + move[0], y + move[1] 
            # nx, ny가 0보다 작거나 n보다 같거나 크면
            if nx < 0 or nx >= n or ny < 0 or ny >= n: 
                # continue
                continue
                
            # graph[nx][ny]가 height보다 크고 nx, ny를 방문하지 않았으면
            if graph[nx][ny] > height and not visited[nx][ny]: 
                # q에 (nx, ny) 삽입
                q.append((nx, ny)) 
                # nx, ny 방문처리
                visited[nx][ny] = True 
                

# 현재 높이 height 1부터 100까지 반복하면서 
for height in range(101): 
    # << 현재 높이 height일때 최대 안전 영역 개수 찾기 >>
    visited = [[False] * n for _ in range(n)]
    # 현재 높이에서 안전 영역 safe 0으로 초기화 
    safe = 0 
    # 인덱스 i: 0부터 n -1 까지 반복하면서
    for i in range(n): 
        # 인덱스 j: 0부터 n - 1 까지 반복하면서 
        for j in range(n):
            # graph[i][j]가 height보다 크면
            if graph[i][j] > height and not visited[i][j]: 
                # bfs 호출 
                # 안전영역 1 증가
                bfs(i, j, height)
                # 안전영역 1 증가
                safe += 1
                
                
    # maxsafe, safe 중 큰 값비교 
    max_safe = max(max_safe, safe) 
                
# max_safe 출력 
print(max_safe)