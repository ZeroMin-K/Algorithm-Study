"""
정사각형으로 이뤄진 N * M 크기 직사각형 맵
육지 또는 바다
캐릭터는 동서남북 중 한곳 바라봄
(A, B) - A: 북쪽으로 떨어진 칸의 개수, B: 서쪽으로 떨어진 칸의 개수 
상, 하, 좌, 우로 이동. 바다로 이동 불가 
1. 현재 위치에서 현재 방향을 기준으로 왼쪽방향(반시계 방향으로 90도 회전햔방향) 부터 차례대로 갈 곳 정함
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면
    왼쪽방향으로 회전한 다음 왼쪽으로 한칸 전진
    왼쪽방향에 가보지 않은 칸이 없다면
        왼쪽 방향으로 회전만 수행, 1단계로 돌아감
#. 네 방향 모두 이미 가본칸이거나 바다로 되어있는 칸인 겨우 
    바라보는 방향을 유지한채로 한 칸 뒤로 가고 1단계 로 돌아감
    뒤쪽방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임 멈춤
바라보는 방향 - 0북쪽, 1동쪽, 2: 남쪽, 3: 서쪽

메뉴얼에 따라 캐릭터 이동시킨 후 캐릭터가 방문한 칸의 수 출력
"""

# 세로크기n, 가로 크기 m공백으로 구분하여 입력
n, m = map(int, input().split())

# 캐릭터의 좌표 (A, B) 바라보는 방향 d가 서로 공백으로 구분하여 입력 
a, b, direction = map(int, input().split())

# 맵 2차원 리스트 생성 
place = []

# n번 반복하며 
for _ in range(n):
    # 한줄씩 입력하며 맵2차원 리스트에 append - (0 육지, 1바다)
    place.append(list(map(int, input().split())))


# 왼쪽으로 방향 회전 함수 - 방향 direction
def rotate_left(direction):
    # [0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽]
    # [0 북쪽 => 서쪽 3, 서쪽 3 => 남쪽 2, 남쪽 2 => 동쪽1, 동쪽 1 => 북쪽 0] [3, 2, 1, 0] - 딕셔너리화
    # 현재 방향에 대해 딕셔너리값 반환
    # next_direction = [0:3, 3:2, 2:1, 1:0]
    # return next_direction[direction]


# 앞으로 이동하는 함수 
def move_forward(x, y, direction): 
    global n
    global m 

    # 현재 방향에서 [북쪽 0 , 동쪽1, 남쪽2,  서쪽3] 앞으로 이동

    # 북쪽: -1, 0 //  동쪽 0, +1 // 남쪽 1, 0 // 서쪽 0,-1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 다음 x,y좌표 
    next_x = x + dx[direction]
    next_y = y + dy[direction]

    if 0 <= next_x and next_x <= n - 1 and 0 <= next_y and next_y <= m - 1:
        return 


# 뒤로 이동하는 함수
def move_backward(x, y, direction):
    pass




# 방문한 칸수 = 0 
count = 0
# 반복하면서
while True:
    # 현재 위치에서 왼쪽 방향 좌표 확인
    # 왼쪽 방향에 가보지 않은 칸이 존재하면 
        # 왼쪽 방향으로 회전 - 바라보는 방향 전환 
        direction = rotate_left(direction)
        # 왼쪽으로 한칸 전진
        # 방문 칸수 증가 

    # 왼쪽 방향에 가보지 않은 칸이 없다면
        # 왼쪽 방향으로 회전 - 바라보는 방향 전환 
        direction = rotate_left(direction)
        # continue

    # 네방향 모두 이미 가본칸인 경우
        # 바라보는 방향에서 뒤에 칸이 바다인 경우
            # break
        # 바라보는 방향 유지한채로 한칸 뒤로 가기
        # continue

# 방문 칸 수 출력 
print(count)