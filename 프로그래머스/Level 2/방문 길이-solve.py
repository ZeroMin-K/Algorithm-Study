"""
게임 캐릭터 4가지 명령어로 움직임
    U: 위쪽 한칸 이동
    D: 아래쪽 한칸 이동
    R: 오른쪽 한칸 이동
    L: 왼쪽 한칸 이동
캐릭터(0, 0)위치에서 시작
경계는 왼쪽위 : (-5, 5), 왼쪽아래 : (-5,-5), 오른쪽위 : (5, 5), 오른쪽 아래 : (5, -5)
    => 길이가 총 11 
지나간길 중 캐릭터가 처음 걸어본 길의 길이 구함 
좌표 평면 경계 넘어가는 명령어 무시 
dirs: 명령어 String 
    - 'U', 'D', 'R', 'L'만 주어짐
    - 길이 500 이하 자연수 
return : 게임 캐릭터가 처음 걸어본 길의 길이 

출발 좌표, 도착좌표를 리스트에 저장하면서 리스트에 있으면 이미가본길이니 pass, 리스트에 없으면 리스트에 저장
저장된 리스트의 길이를 반환 
"""
def solution(dirs):
    # U, D, R, L에 대한 좌표 딕셔너리
    moves = {'U' : (-1, 0), 'D' : (1, 0), 'R' : (0, 1), 'L' : (0, -1)}
    # 출발 좌표, 도착좌표들을 저장하는 길 paths 리스트 빈리스트로 생성 
    paths = [] 
    # 시작 위치 x, y는 5, 5 (경계 넘어가는지 쉽게 계산하기 위해 (-5, 5)를 (0, 0)으로 치환)  
    x, y = 5, 5
    # dirs를 하나씩 탐색하면서 : 원소 dir 
    for dir in dirs: 
        # 다음 x좌표 nx, y좌표 ny는 x + moves[dir][0], y + move[dir][1]
        nx, ny = x + moves[dir][0], y + moves[dir][1]
        # nx, ny가 0보다 같거나 크고 11보다 작으면 
        if 0 <= nx < 11 and 0 <= ny < 11: 
            # ((x, y), (nx, ny)), ((nx, ny), (x, y))가 둘다 paths에 없으면
            if ((x, y), (nx, ny)) not in paths and ((nx, ny), (x, y)) not in paths: 
                # paths에 ((x, y), (nx, ny)) 삽입
                paths.append(((x, y), (nx, ny)))
                # paths에 ((nx, ny), (x, y)) 삽입 
                paths.append(((nx, ny), (x, y)))
                
            # x, y를 nx, ny로 초기화
            x, y = nx, ny
    
    # paths의 길이 /2 리턴 
    return len(paths) // 2