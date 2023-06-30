"""
n * n 크기의 복도. 1 * 1 크기로 나누어짐. 특정위치 선생, 학생, 장애물 위치
선생들은 상, 하, 좌, 우 4가지 방향으로 감시 진행
복도에 장애물 위치시 장애물뒤 학생 못봄.
4가지 방향에 대해 아무리 멀리 있어도 막히기 전까지 모두 볼 수 있다고 가정
선생 존재 칸 T, 학생 존재 칸 S, 장애물 존재칸 O 
복도의 빈칸 중 장애물 설치할 위치 골라 정확히 3개 장애물 설치
모든 학생들은 감시로부터 피할 수 있는지 여부에 대한것을 출력 

백트래킹을 이용하여 빈칸에다 장애물을 설치하고 
장애물을 3개 설치했을때 선생위치로부터 감시 시작
감시했을때 아무도 들키지 않는지 확인 
"""

# 복도 크기 n 입력
n = int(input())
# 복도 위치정보를 저장하는 리스트 board 빈 리스트로 초기화 
board = [] 
# 선생들의 위치를 저장하는 리스트 teachers 빈리스트로 초기화 
teachers = [] 
# 인덱스 i: 0부터 n - 1까지 반복하면서 
for i in range(n): 
    # n개의 원소를 공백구분하여 리스트 data로 입력
    data = list(input().split())
    # data를 board에 append
    board.append(data)
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(n):
        # data[j]가 'T'이면 (선생이면 위치정보 저장) 
        if data[j] == 'T':
            # teachers에 (i, j) append
            teachers.append((i, j))

# 선생이 상, 하, 좌, 우 감시하는 방향에 대한 moves 리스트
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 한번이라도 피할 수 있는지 여부 total_avoid False로 초기화           
total_avoid = False
# 현재 세워진 장애물 개수 num_obs 0으로 초기화 
num_obs = 0 

def watch(board):
    round_avoid = True
    
    # teachers를 하나씩 탐색하면서 - 원소 teacher
    for teacher in teachers:
        # moves를 하나씩 탐색하면서 - 원소 move (현재 위치에서 상, 하, 좌, 우로만 이동)
        for move in moves:  
            # 다음 x좌표 nx는 teacher[0] + move[0]
            nx = teacher[0] + move[0] 
            # 다음 y좌표 ny는 teacher[1] + move[1] 
            ny = teacher[1] + move[1]
                        
            # nx와 ny가 0보다 같거나 크고 n보다 작은 동안
            while 0 <= nx < n and 0 <= ny < n: 
                # board[nx][ny]가 'O'이면 (장애물이면) 
                if board[nx][ny] == 'O':
                    # 현재 방향에 대한 감시 종료 break
                    break
                # board[nx][ny]가 'S'이면 
                elif board[nx][ny] == 'S':
                    # round_avoid False로 변경
                    round_avoid = False 
                    break
                # 이동가능하면 
                else:
                    # 상, 하, 좌,우 한방향 그대로 이동해서 다음 좌표 갱신 
                    nx += move[0]
                    ny += move[1]
    
    return round_avoid 

def install_walls(num_obs, board):
    global total_avoid 
    
    # 장애물 3개 설치하면 
    if num_obs == 3:
        # 감시 진행 - 피할 수있으면 
        if watch(board):
            # 한번이라도 피할 수 있음
            total_avoid = True
        
        return 
        
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                install_walls(num_obs + 1, board)
                board[i][j] = 'X'
        
install_walls(0, board) 

# total_avoid가 True이면 YES, False이면 "NO" 출력
if total_avoid:
    print("YES")
else:
    print("NO")