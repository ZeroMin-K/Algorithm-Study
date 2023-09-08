"""
2 * 2 블록들을 찾아내면서 블록들 지우고 지운 블록 세고 밑으로 블록 내리기를
2 * 2 블록이 없을때까지 반복 진행하기 
"""
# 현재 좌표로부터 오른쪽, 아래쪽, 대각선 아래쪽 좌표에 대한 리스트
nears = [(0, 1), (1, 0), (1, 1)]

# 현재 좌표에서 2 * 2 블록을 찾았는지 여부를 리턴하는 함수 find_blocks: 매개변수 i, j, board
def find_blocks(i, j, board):
    m = len(board)
    n = len(board[0])
    # 현재 위치에서 문자 board[i][j] 
    # 현재  위치에서 2 * 2 블록 좌표 담는 리스트 same_blocks 빈 리스트로 초기화 
    same_blocks = [] 
    # same_blocks에 (i, j) 삽입 
    same_blocks.append((i, j))
    # nears를 하나씩 탐색하면서: 원소 near
    for near in nears: 
        # nx, ny는 i + near[0], j + near[1]
        nx, ny = i + near[0], j + near[1] 
        # nx가 0보다 작거나 m보다 같거나 크거나 ny가 0보다 작거나 n보다 같거나 크거나
        # board[i][j]와 board[nx][ny]가 다르면
        if nx < 0 or nx >= m or ny < 0 or ny >= n or \
            board[i][j] != board[nx][ny]:
            # 빈 리스트 리턴 
            return []
        # board[i][j]와 board[nx][ny]가 같으면
        elif board[i][j] == board[nx][ny]:
            # same_blocks에 (nx, ny) 삽입 
            same_blocks.append((nx, ny))
    
    # same_blocks 리턴
    return same_blocks

# 판에서 2 * 2 블록들을 제거하는 함수 remove_blocks: 매개변수 removed_blocks, board
# 제거된 블록 개수 리턴 
def remove_blocks(removed_blocks, board):
    # 제거된 블록수 removed_block_num 0으로 초기화 
    removed_block_num = 0 
    # removed_blocks를 하나씩 탐색하면서 : 원소 x, y 
    for x, y in removed_blocks:
        # 해당 위치 빈 공간으로 표시
        board[x][y] = 0 
        # removed_block_num 1 증가 
        removed_block_num += 1
        
    # removed_block_num 리턴
    return removed_block_num 
            
# 판에서 블록들을 아래로 떨어뜨리는 함수 fall_blocks : 매개변수 m, n, board
def fall_blocks(m, n, board): 
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(n): 
        # 인덱스 i: m - 1부터 1까지 반복하면서 
        for i in range(m - 1, 0, -1): 
            # 위쪽 블록의 행 prev는 i - 1
            prev = i - 1
            # prev가 0행 이상이고 board[i][j]가 비어있는 동안
            while prev >= 0 and board[i][j] == 0: 
                # board[i][j]의 값은 board[prev][j]
                board[i][j] = board[prev][j]
                # board[prev][j]는 0
                board[prev][j] = 0 
                # prev 1 감소 
                prev -= 1

def solution(m, n, board):
    # 처리하기 쉽도록 board를 블록 문자를 원소로하는 2차원 리스트로 변경 
    board = [list(block) for block in board]
    # 지운 블록 수 removed_block_num 0으로 초기화 
    removed_block_num = 0 
    
    # 2 * 2 블록을 찾았는지 여부 is_found True로 초기화 
    is_found = True 
    # << 2 * 2 블록이 없을 때까지 반복 진행 >>
    # is_found가 True인 동안 진행 
    while is_found: 
        # is_found False로 초기화 (초기에 2 * 2 블록을 못찾은 것으로 가정) 
        is_found = False 
        # 지워야할 모든 2 * 2 블록의 좌표를 저장하는 set removed_blocks 빈 set로 초기화 
        removed_blocks = set() 
        # 현재 위치에서부터 2 * 2 블록의 좌표를 저장하는 리스트 found_blocks 빈리스트로 초기화 
        found_blocks = [] 
        # << 2 * 2 블록이 있는지 확인 >>
        # 인덱스 i: 0부터 m - 1까지 반복하면서 
        for i in range(m): 
            # 인덱스 j: 0부터 n - 1까지 반복하면서 
            for j in range(n): 
                # board[i][j]가 비어있으면
                if board[i][j] == 0:
                    # continue 
                    continue 
                # find_blocks를 통해 i, j에서 2 * 2 블록을 찾아 found_blocks로 리턴 
                found_blocks = find_blocks(i, j, board)
                # found_blocks가 비어있지 않으면 
                if found_blocks:
                    # is_found True로 초기화 
                    is_found = True 
                    # found_blocks를 하나씩 탐색하면서 : 원소 block
                    for block in found_blocks:
                        # removed_block에 삽입 
                        removed_blocks.add(block)
        
        #  << 2 * 2 블록이 없으면 반복 종료 >>
        # is_found가 False이면
        if not is_found: 
            # break
            break 
            
        # << 2 * 2 블록들을 찾아내서 지우면서 세기 >>
        # remove_blocks 호출하여 removed_block_num에 더함 : 인자 removed_blocks, board
        removed_block_num += remove_blocks(removed_blocks, board)

        # << 지워진 블록들에 대해 판 밑으로 떨어뜨리기 >> 
        # fall_blocks 호출 (인자 m, n, board)
        fall_blocks(m, n, board)
    
    return removed_block_num