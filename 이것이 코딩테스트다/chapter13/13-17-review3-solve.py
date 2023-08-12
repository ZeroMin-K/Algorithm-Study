"""
n * n 크기 시험관 - 1 * 1 크기 칸으로 나누어짐
특정위치 바이러스 존재. 
1번부터 k번까지 바이러스 종류 중 하나에 속함 
바이러스는 1초마다 상, 하, 좌, 우 방향으로 증식
매초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
특정칸에 이미 바이러스 존재시 다른 바이러스 들어갈 수 없음

s초가 지난 후 (x, y)에 존재하는 바이러스 종류 출력
- 바이러스가 존재하지 않으면 0 출력
- x, y 는 각 행과 열의 위치 
- 시험관의 가장 왼쪽위에 해당하는 곳은 (1, 1)에 해당

각 바이러스들을 bfs로 탐색
바이러스 종류와 시간을 따져가면서 s초까지 퍼뜨림
"""

# sys import
import sys 
# input 메서드를 sys stdin readline메서드로 변환
input = sys.stdin.readline

# n, k 입력
n, k = map(int, input().split())
# 시험관 원소들을 저장할 graph 빈 리스트로 생성 
graph = [] 
# 시험관에서 각 칸마다 시간들을 저장하는 times 값을 10001로 갖고 n * n 크기의 리스트로 생성 
times = [[10001] * n for _ in range(n)]
# 바이러스 위치들을 저장하는 viruses 빈 리스트로 생성 
viruses = [] 
# 인덱스 i: 0부터 n - 1까지 반복하면서 
for i in range(n):
    # 공백 구분을 n개의 원소 한 줄 data 입력 
    data = list(map(int, input().split()))
    # data를 graph에 삽입
    graph.append(data)
    # 인덱스 j: 0부터 n - 1까지 반복하면서  
    for j in range(n):
        # data[j]가 0이 아니면 
        if data[j] != 0:
            # (i, j)를 viruses에 삽입 
            viruses.append((i, j))
            # times[i][j]를 0으로 초기화 (바이러스 퍼지기 시작시간)
            times[i][j] = 0 

# s, x, y 공백을 기준으로 구분 
s, x, y = map(int, input().split())

# 상, 하, 좌, 우 이동할때 x,y 변화값 리스트 moves 
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# deque import 
from collections import deque
# bfs 함수 선언 : 매개변수 start_x, start_y
def bfs(start_x, start_y):
    # 큐 q deque로 생성
    q = deque()
    # q에 시작 위치 (start_x, start_y) 삽입
    q.append((start_x, start_y))
    # 현재바이러스 종류 virus_type 는 graph[start_x][start_y]
    virus_type = graph[start_x][start_y]
    
    # 큐가 빌 때까지 반복하면서 
    while q: 
        # q에서 왼쪽에서 pop한 현재 좌표 x, y
        x, y = q.popleft()
        
        # times[x][y]가 s보다 같거나 크면
        if times[x][y] >= s:
            # continue (현재 좌표에서 더이상 이동불가)
            break
        
        # 다음좌표로 이동할때 시간 next_time times[x][y] + 1로 초기화
        next_time = times[x][y] + 1
        
        # moves를 하나씩 탐색하면서 : 원소 move
        for move in moves:
            # 다음 x좌표 next_x는 x + move[0]
            next_x = x + move[0]
            # 다음 y좌표 next_y는 y + move[1]
            next_y = y + move[1]
            
            # next_x가 0보다 작거나 next_y가 0보다 작거나 next_x가 n보다 크거나 같거나
            # \ next_y가 n보다 크거나 같으면 (좌표를 벗어남)
            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n: 
                # continue 
                continue 
            
            # graph[next_x][next_y] 가 0이거나 \
            # \ times[next_x][next_y]가 next_time보다 크거나 
            # \ times[next_x][next_y]가 next_time과 같고 graph[next_x][next_y]가 virus보다 크면
            if graph[next_x][next_y] == 0 or \
                times[next_x][next_y] > next_time or \
                (times[next_x][next_y] == next_time and graph[next_x][next_y] > virus_type):
                # graph[next_x][next_y]는 현재 virus로 값 변경
                graph[next_x][next_y] = virus_type 
                # times[next_x][next_y]는 next_time로 값 변경
                times[next_x][next_y] = next_time 
                # q에 (next_x, next_y) 삽입 
                q.append((next_x, next_y))
            
# viruses를 하나씩 탐색하면서 : 원소 virus
for virus in viruses: 
    # virus를 인자로 bfs 호출
    bfs(virus[0], virus[1])


# s초뒤에 (x - 1, y - 1)에 존재 하는 바이러스 종류 출력 (존재하지 않으면 0출력)
print(graph[x - 1][y - 1])