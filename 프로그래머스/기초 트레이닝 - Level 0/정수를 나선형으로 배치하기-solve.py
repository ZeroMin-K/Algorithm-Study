def solution(n):
    answer = [[0] * n for _ in range(n)]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num, end = 2, n * n 
    x, y, dir = 0, 0, 0
    answer[x][y] = 1
    
    while num <= end: 
        nx, ny = x + moves[dir][0], y + moves[dir][1]
        
        if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
            answer[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            dir = (dir + 1) % len(moves)
        
    return answer