"""
정사각형 모양의 지도 - 1은 집이 있는 곳, 0은 집이 없는곳
연결된 집의 모임인 단지 정의. 단지에 번호 붙임
상하좌우만 연결
bfs진행하면서 방문하지 않은 곳들은 단지에 맞춰 진행
첫 bfs진행시 단지도 포함해서 진행
"""

# 지도의 크기 입력
n = int(input())

# 집 리스트 저장하는 그래프
graph = [] 

# n번 반복하며
for _ in range(n):
    # 각 단지정보 입력 
    data = list(map(int, input()))
    graph.append(data)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

# bfs 진행 - 현재 단지번호, 시작위치 
def bfs(x, y):
    # 큐 생성
    q = deque()
    # 현재 위치 큐에 삽입
    q.append((x,y))
    # 현재 위치를 단지번호로 변경
    graph[x][y] = 2
    # 현재 단지 개수 1
    count_apt = 1

    # 큐가 빌때까지 반복
    while q: 
        # 큐에서 빼온 다음좌표
        x, y = q.popleft()

        # 다음좌표에서 상, 하, 좌, 우 확인하며
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 인덱스에 맞는 위치이고
            if 0 <= next_x < n and 0 <= next_y < n:
                # 방문하지 않은 곳이면
                if graph[next_x][next_y] == 1:
                    # 큐에 삽입
                    q.append((next_x, next_y))
                    # 현재 단지로 변경 
                    graph[next_x][next_y] = 2
                    # 현재 단지 개수 증가
                    count_apt += 1
    
    # 현재 단지 개수 반환 
    return count_apt

# 총 단지 수 
total = 0 
results = [] 
# 인덱스 i : n행만큼 반복
for i in range(n):
    # 인덱스 j : n열만큼 반복
    for j in range(n):
        # i, j에서 1이면
        if graph[i][j] == 1:
            # 단지 수 증가
            total += 1
            # bfs 진행 - 현재 단지 수 
            count = bfs(i, j) 
            results.append(count)

# 총 단지 수출력
print(total)

results.sort()
# 각 단지내 집의 수를 오름차순 정렬하여 한줄에 하나씩 출력 
for result in results:
    print(result)