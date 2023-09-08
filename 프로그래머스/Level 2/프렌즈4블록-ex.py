def find_blocks(i, j, board):
    m, n = len(board), len(board[0])
    same_blocks = [(i, j)]
    
    for dx, dy in [(0, 1), (1, 0), (1, 1)]:
        nx, ny = i + dx, j + dy
        if nx < 0 or nx >= m or ny < 0 or ny >= n or board[i][j] != board[nx][ny]:
            return []
        same_blocks.append((nx, ny))
    
    return same_blocks

def remove_blocks(removed_blocks, board):
    removed_block_num = 0 
    for x, y in removed_blocks:
        board[x][y] = 0 
        removed_block_num += 1
    return removed_block_num 

def fall_blocks(m, n, board): 
    for j in range(n): 
        for i in range(m - 1, 0, -1): 
            prev = i - 1
            while prev >= 0 and board[i][j] == 0: 
                board[i][j], board[prev][j] = board[prev][j], board[i][j]
                prev -= 1

def solution(m, n, board):
    board = [list(row) for row in board]  # 문자열 리스트를 2D 문자열 배열로 변환
    removed_block_num = 0 
    
    while True: 
        is_found = False 
        removed_blocks = set() 
        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == 0:
                    continue 
                found_blocks = find_blocks(i, j, board)
                if found_blocks:
                    is_found = True 
                    removed_blocks.update(found_blocks)
        
        if not is_found: 
            break 
            
        removed_block_num += remove_blocks(removed_blocks, board)
        fall_blocks(m, n, board)
    
    return removed_block_num