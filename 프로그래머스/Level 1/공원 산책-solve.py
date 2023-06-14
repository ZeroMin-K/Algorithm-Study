"""
격자 모양 공원 명령에 따라 산책 진행
명령 수행전 두가지 확인
    1. 이동시 공원을 벗어나는지 확인
    2. 장애물을 만나는지 확인
    두가지 하나라도 해당되면 해당 명령 무시, 다음 명령 수행
공원 가로 길이 W, 세로길이 H, 좌측 상단 (0, 0), 우측 하단 (H - 1, W - 1) 

park: 공원을 나타내는 문자열 배열
    S: 시작 지점, 길 : 'O', 장애물 : 'X'. 격자 모양 공원
routes: 수행할 명령이 담긴 문자열 배열
    "op n" 구조 ["방향 거리", "방향 거리"]
    N: 북쪽, S: 남쪽, W: 서쪽, E: 동쪽
return : 모든 명령 수행후 위치를 [세로방향, 가로방향 좌표] 배열

routes를 하나씩 확인하면서 park의 좌표에 따라 
공원 벗어나는지, 장애물 만나는지 확인하고 그에 따라 무시하거나 이동 후 좌표 리턴 
"""

def is_proper(park, x, y):
    # 다음 x좌표가 0보다 크거나 같고 park의 길이보다 작고, 다음 y좌표가 0보다 크거나 같고 park[0]의 길이보다 작으면
    if 0 <= x < len(park) and 0 <= y < len(park[0]):
        # park[다음 x좌표][다음 y좌표]에서 값이 'O'이면
        if park[x][y] == 'O':
            # 이동 가능함
            return True 

    # 이동 불가 
    return False

def solution(park, routes):
    answer = []
    
    # 이동 후 좌표 위치 출발위치로 초기화 
    # 출발위치 찾기
    x, y = 0, 0
    # 인덱스 i - 0부터 park길이 - 1까지 반복하면서
    for i in range(len(park)):
        # 인덱스 j - 0부터 park[i] 길이 - 1까지 반복하면서
        for j in range(len(park[i])):
            # park[i][j] 가 'S'이면
            if park[i][j] == 'S':
                # 현재 위치 = i, j
                x, y = i, j
                # park[i][j]를 'O'으로 변경
                park[i] = park[i].replace('S', 'O')
                
    # 동 E : 0, 서 W : 1, 남 S : 2, 북 N : 3으로 각 문자, 인덱스를 키값으로 갖는 방향 딕셔너리 directions
    directions = {'E' : 0, 'W' : 1, 'S' : 2, 'N' : 3}
    # 동, 서, 남, 북 이동시 x 좌표 증가값 리스트 dx
    dx = [0, 0, 1, -1]
    # 동, 서, 남, 북 이동시 y 좌표 증가값 리스트 dy 
    dy = [1, -1, 0, 0]
    
    # routes를 하나씩 탐색하면서 - 원소 route
    for route in routes: 
        # route를 방향 op, 이동하는 칸 n으로 분리
        op, n = route[0], int(route[2])    
        # 명령 이동 가능 여부
        can_move = True     
        # 이동 후 위치를 현재 위치로 초기화 - 이동하면서 중간중간 확인
        nx, ny = x, y 
        
        # n번 만큼 이동
        for _ in range(n): 
            # 다음 x 좌표는 현재 x좌표에서 op를 키로 directions에서 그 값을 인덱스로 하여 dx값을 더함
            nx += dx[directions[op]]
            # 다음 y 좌표는 현재 y좌표에서 op를 키로 directions에서 그 값을 인덱스로 하여 dy값을 더함
            ny += dy[directions[op]]
            
            # 다음 좌표를 이동 불가능하면 
            if not is_proper(park, nx, ny):
                # 현재 명령 무시 
                can_move = False
                # 이동안함 
                break
        
        # 이동할 수 있다면 
        if can_move: 
            # 좌표 이동
            x, y = nx, ny 
    
    # [x좌표, y좌표] 리턴 
    return [x, y]