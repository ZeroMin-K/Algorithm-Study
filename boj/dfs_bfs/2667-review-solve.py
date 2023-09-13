"""
정사각형 모양의 지도
1: 집이 있는 곳, 0: 집이 없는 곳
연결된 집의 모임인 단지 정의
단지에 번호 붙임
연결되었다는 것은 좌우, 아래위로 다른 집이 있는 경우
지도를 입력하여 단지수 출력
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력 
"""

# 지도 크기 n 입력
n = int(input()) 
# graph 빈리스트로 초기화 
graph = [] 
# n번 반복하면서 
for _ in range(n): 
    # 문자열을 입력받아 graph에 삽입
    graph.append(list(map(int, list(input()))))

# 상, 하, 좌, 움 리스트 moves
moves = [(1, 0), (-1, 0), (0, -1), (0, 1)]

from collections import deque 

# bfs함수 선언 : 매개 변수 i, j, apt_num
def bfs(i, j, apt_num): 
    # 큐 q deque로 생성 
    q = deque() 
    # graph[i][j]값을 apt_num으로 변경
    graph[i][j] = apt_num 
    # 큐에 (i, j) 삽입
    q.append((i, j)) 
    # 현재 같은 단지 수 apts 1로 초기화 
    apts = 1
    
    # q가 빌때까지 반복하며
    while q:
        # 현재 좌표 x, y는 q에서 popleft한 값
        x, y = q.popleft() 
        
        # moves를 하나씩 탐색하며 : 원소 move
        for move in moves: 
            # 다음 좌표 nx, ny는 x + move[0], y + move[1]
            nx, ny = x + move[0], y + move[1] 
            
            # nx, ny가 0보다 작거나 n보다 같거나 크면
            if nx < 0 or ny < 0 or nx >= n or ny >= n: 
                # continue
                continue 
                
            # graph[nx][ny]가 1이면
            if graph[nx][ny] == 1: 
                # graph[nx][ny]는 apt_num으로 갱신
                graph[nx][ny] = apt_num 
                # q에 (nx, ny) 삽입 
                q.append((nx, ny)) 
                # apts 1씩 증가
                apts += 1
    
    # apts 리턴 
    return apts 

# 현재 단지 번호 : 2
apt_num = 2
# 각 단지 집수 houses 빈리스트로 초기화 
houses = [] 

# 인덱스 i: 0부터 n - 1까지 반복하면서
for i in range(n): 
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(n): 
        # graph[i][j]가 1이면
        if graph[i][j] == 1: 
            # bfs 진행 후 houses에 리턴 값 삽입 
            houses.append(bfs(i, j, apt_num))
            # apt_num 1 증가 
            apt_num += 1
    
# << 총 단지수 출력 >>
# houses의 길이 출력
print(len(houses))

# << 각 단지내 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력 >>
# houses 오름차순정렬
houses.sort() 
# houses 값을 한줄씩 출력 
for house in houses: 
    print(house)