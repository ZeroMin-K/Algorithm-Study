"""
1 * 1 크기의 사각형으로 이루어진 직사각형 격자 형태의 지도 
x : 바다, 숫자 : 무인도 
상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도 이룸
숫자는 식량을 나타냄
상, 하, 좌, 우로 연결되는 칸에 적힌 숫자 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물수있는지
maps: 지도 나타내는 문자열 배열
return : 각 섬에서 최대 며칠씩 머무를수있는지 오름차순 배열 
    - 지낼수있는 무인도가 없다면 -1 
    
BFS를 통해서 각 무인도를 탐색하며 숫자들 합하며 리스트에 저장하고 오름차순 정렬 
"""

def solution(maps):
    # maps의 가로길이 n, maps의 세로 길이 m
    n, m = len(maps), len(maps[0]) 
    # 방문했는지 여부 확인하는 visited 값은 False로 n * m 2차원 리스트로 생성 
    visited = [[False] * m for _ in range(n)]

    # 상, 하, 좌, 우로 좌표 이동에 대한 리스트 moves 생성 
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # deque import 
    from collections import deque 
    # bfs 선언: 매개변수 start_x, start_y
    def bfs(start_x, start_y): 
        # 현재까지 머물수있는 일수 stay maps[start_x][start_y] 값으로 초기화
        stay = int(maps[start_x][start_y])
        # 큐 q deque로 생성
        q = deque() 
        # q에 (start_x, start_y) 삽입
        q.append((start_x, start_y))
        # (start_x, start_y) 방문 처리 
        visited[start_x][start_y] = True 
        
        # q가 빌 때까지 반복 
        while q: 
            # x, y는 q에서 popleft한값
            x, y = q.popleft() 
            
            # moves를 하나씩 탐색하면서: 원소 move
            for move in moves: 
                # nx, ny 는 x + move[0], y + move[1]
                nx, ny = x + move[0], y + move[1]
                
                # nx, ny가 0보다 작거나 nx가 n보다 같거나 크거나, ny가 m보다 같거나 크면
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    # continue
                    continue 
                    
                # maps[nx][ny]가 'X'가 아니고 방문한적없으면 
                if maps[nx][ny] != 'X' and not visited[nx][ny]:
                    # stay에 maps[nx][ny] 더함
                    stay += int(maps[nx][ny])
                    # q에 (nx, ny) 삽입 
                    q.append((nx, ny))
                    # (nx, ny) 방문처리
                    visited[nx][ny] = True 
                    
        # stay 리턴
        return stay 
    
    # 각 무인도마다 최대 며칠씩 머물 수있는 저장하는 stays 빈리스트로 저장 
    stays = [] 
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n): 
        # 인덱스 j: 0부터 m - 1까지 반복하면서 
        for j in range(m):
            # maps[i][j]가 X가 아니고 방문한 적 없으면 
            if maps[i][j] != 'X' and not visited[i][j]: 
                # BFS 실행하여 무인도의 숫자 합 리턴한 값 stay
                stay = bfs(i, j) 
                # stay를 stays에 삽입
                stays.append(stay) 
                
    # stays가 비어있으면 -1 삽입 
    if not stays: stays.append(-1)
    
    # stays를 오름차순 정렬하여 리턴 
    return sorted(stays)