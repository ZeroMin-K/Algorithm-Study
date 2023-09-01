"""
5 * 5 크기의 맵 
캐릭터가 1행 1열에 위치. 상대는 5행 5열에 위치 
검은색 : 벽으로 막혀 못감. 흰색 : 갈 수 있는길
캐릭터는 동, 서, 남, 북 방향으로 한칸씩이동.
maps: 게임 맵의 상태
    - n * m 크기의 게임 맵 상태 2차원 배열 
    - 0 : 벽, 1 : 벽이 없는 자리 
return : 캐릭터가 상대팀 진영에 도착하기 위해 지나가야하는 칸의 개수 최솟값 
    - 도착할 수 없을 때 -1 
한칸씩 맵안에서 상, 하, 좌, 우로 움직이니 BFS를 통해서 상, 하, 좌, 우로 탐색하며
다음 좌표에서 거리는 현재 거리에서 + 1만큼 움직인 것 
0이면 이동 불가, 1이면 이동, 1보다 크면 현재 거랑 비교해서 작은거로 기록 
"""
# deque import 
from  collections import deque

# 상, 하, 좌, 우로 움직일 때 좌표변화에 대한 리스트 moves
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# bfs 함수 선언 : 매개변수 맵 maps, n, m
def bfs(maps, n, m): 
    # 큐 q deque로 선언
    q = deque() 
    # (0, 0)을 q에 삽입
    q.append((0, 0))
    
    # q가 빌 때까지 반복 
    while q: 
        # q에서 popleft한 x, y
        x, y = q.popleft()
        # moves를 하나씩 탐색하면서: 원소 move
        for move in moves: 
            # 다음 좌표 nx는 x + move[0]
            nx = x + move[0] 
            # 다음 좌표 ny는 y + move[1]
            ny = y + move[1] 
            # 다음 좌표까지 이동 거리 dist는 maps[x][y] + 1
            dist = maps[x][y] + 1
            
            # nx가 0보다 작거나 ny가 0보다 작거나 nx가 n보다 같거나 크거나 ny가 m보다 같거나 크면
            # 또는 maps[nx][ny]가 0이면 (벽이면) 
            if nx < 0 or ny < 0 or nx >= n or ny >= m or \
                maps[nx][ny] == 0: 
                # continue
                continue 
            
            # maps[nx][ny]가 1이거나 maps[nx][ny]가 dist보다 크면
            if maps[nx][ny] == 1 or maps[nx][ny] > dist: 
                # maps[nx][ny]값은 dist로 변경
                maps[nx][ny] = dist 
                # (nx, ny)를 q에 삽입
                q.append((nx, ny)) 

def solution(maps):
    # maps의 길이 n
    n = len(maps) 
    # maps[0]의 길이 m
    m = len(maps[0]) 
    # bfs 호출 
    bfs(maps, n, m)
    # maps[n - 1][m - 1]이 1보다 크면 maps[n - 1][m - 1] 리턴
    # 작으면 -1 리턴 
    return maps[n - 1][m - 1] if maps[n - 1][m - 1] > 1 else -1