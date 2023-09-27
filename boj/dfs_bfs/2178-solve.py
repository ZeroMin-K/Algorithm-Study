"""
n * m 크기 배열로 표현되는 미로
1 : 이동 가능한 칸, 0 : 이동 불가 칸
(1, 1)에서 출발하여 (n, m)위치로 이동할때 최소 칸수 
한칸에서 다른칸으로 이동할때 서로 인접한 칸으로만 이동
시작 위치, 도착 위치도 포함 

bfs를 이용해서 이동경로를 탐색하며 현재까지 왓을때 최소 거리를 이용
"""
# 빠른 입력 
import sys
input = sys.stdin.readline 

# n, m 입력 
n, m = map(int, input().split()) 
# 현재 미로 graph 빈리스트로 생성
graph = [[0] * m for _ in range(n)]
# n번 반복하면서 
for i in range(n): 
    # 한 줄을 입력받아 int변환후 리스트로 바꿔 graph에 삽입
    data = input() 
    for j in range(m):
        graph[i][j] = int(data[j])
    
# deque import
from collections import deque 
# q dque로 생성
q = deque() 
# (0, 0)을 q에 삽입 
q.append((0, 0))
# 상, 하, 좌, 우로 움직이는 moves 리스트 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 큐가 빌때까지 반복하면서 
while q: 
    # x, y 는 q에서 popleft
    x, y = q.popleft() 
    # 다음 위치까지 거리 next는 graph[x][y] + 1
    next = graph[x][y] + 1
    # moves를 하나씩 탐색하면서 : 원소 move
    for move in moves: 
        # nx, ny는 x + move[0], y + move[1]
        nx, ny = x + move[0], y + move[1] 
        
        # nx가 0보다 작거나 n보다 같거나 크거나 ny가 0보다 작거나 m보다 같거나 크면
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            # continue
            continue 
            
        # graph[nx][ny]가 1이거나 graph[nx][ny]보다 next가 작으면 
        if graph[nx][ny] == 1 or graph[nx][ny] > next: 
            # graph[nx][ny]는 next
            graph[nx][ny] = next
            # q에 (nx, ny) 삽입
            q.append((nx, ny)) 
            
# graph[n - 1][m - 1] 출력 
print(graph[n - 1][m - 1])