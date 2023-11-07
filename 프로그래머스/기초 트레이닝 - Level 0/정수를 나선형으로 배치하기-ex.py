def solution(n):
    answer = [[None] * n for _ in range(n)]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y, dir = 0, 0, 0
    
    for i in range(1, n ** 2 + 1):
        answer[x][y] = i
        if x + moves[dir][0] >= n or y + moves[dir][1] >= n or answer[x + moves[dir][0]][y + moves[dir][1]]:
            dir = (dir + 1) % len(moves)
        x, y = x + moves[dir][0], y + moves[dir][1]
    
    return answer