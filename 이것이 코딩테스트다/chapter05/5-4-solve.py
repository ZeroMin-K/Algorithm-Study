"""
n * m 크기 직사각형 미로 탈출하기
위치 (1, 1), 출구(n, m)위치 한번에 한칸 씩 이동
괴물 0, 괴물없으면 1
미로는 반드시 탈출 가능
탈출위한 최소 칸의 개수 (시작 칸, 마지막 칸 모두 포함)

현재 칸에서 다음칸 이동할때마다 한칸씩 더해서 거리 확인
bfs로 확인 
"""
from collections import deque

# n, m 미로 크기 입력
n, m = map(int, input().split())

# 미로 그래프 초기화
miro = [] 

# n만큼 반복하며
for _ in range(n):
    # 한줄씩 읽어 list로 만들어 미로그래프에 append
    miro.append(list(map(int, input())))

# bfs함수 - start, visited
def bfs():
    # 큐 생성
    q = deque()
    # 현재 위치를 큐에 넣기 
    q.append((0, 0))

    # 큐가 빌때까지 반복
    while q:
        # 큐에서 꺼냄 
        x, y = q.popleft()

        # dx - 상, 하, 좌, 우 이동
        dx = [-1, 1, 0, 0]
        # dy - 상, 하, 좌, 우 이동 
        dy = [0, 0, -1, 1]

        # 상, 하, 좌우 반복하면서
        for i in range(4):
            # 다음 좌표 확인
            next_x = x + dx[i]
            next_y = y + dy[i] 
            # 다음좌표가 미로 인덱스에 맞으면
            if 0 <= next_x and next_x <= n -1 and 0 <= next_y and next_y <= m - 1:
                # 다음칸이 방문하지 않은 칸이면
                if miro[next_x][next_y] == 1:
                    # 현재칸은 이전칸 + 1
                    miro[next_x][next_y] += miro[x][y]
                
                    # 현재 칸을 큐에 삽입 
                    q.append((next_x, next_y))

# 현재 위치에서 bfs 진행
bfs()

# (n, m) 위치에서 값 출력 
print(miro[n-1][m-1])