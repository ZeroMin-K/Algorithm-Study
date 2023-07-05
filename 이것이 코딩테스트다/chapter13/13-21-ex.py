from collections import deque

# 땅의 크기n, l, r 입력
n, l, r = map(int, input().split())

# 전체 나라 정보(n * n) 입력
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신 
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보 담는 리스트
    united = []
    united.append((x,y))

    # bfs를 위한 큐 자료구조 정의 
    q = deque()
    q.append((x, y))
    union[x][y] = index         # 현재 연합 번호 할당
    summary = graph[x][y]       # 현재 연합의 전체 인구 수 
    count = 1                   # 현재 연합의 국가 수

    # 큐가 빌때 까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 바로 옆에 있는 나라 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구차이가 l명이상, r명이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    # 연합 국가끼리 인구 분배
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

# 더이상 인구 이동할 수 없을때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            # 해당 나라가 아직 처리되지않았다면
            if union[i][j] == -1:      
                process(i, j, index)
                index += 1
    # 든 인구 이동이 끝난 경우
    if index == n * n :
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)