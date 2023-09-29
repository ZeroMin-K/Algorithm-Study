def solution(n):
    moves = [(1, 0), (0, 1), (-1, -1)]
    tri = [[0] * i for i in range(1, n + 1)]
    x, y = 0, 0
    num = 1
    dir = 0
    
    while num <= (n + 1) * n // 2:
        tri[x][y] = num 
        nx, ny = x + moves[dir][0], y + moves[dir][1]
        num += 1
        if 0 <= nx < n and 0 <= ny <= nx and tri[nx][ny] == 0:
            x, y = nx, ny 
        else:
            dir = (dir + 1) % 3
            x, y = x + moves[dir][0], y + moves[dir][1]

    return sum(tri, [])