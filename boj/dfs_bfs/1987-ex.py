import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [] 
for _ in range(r): 
    board.append(list(input()))
    
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 1

def bfs(start_x, start_y):
    global answer 
    q = set([(start_x, start_y, board[start_x][start_y])])
    while q:
        x, y, alphas = q.pop() 
        for move in moves: 
            nx, ny = x + move[0], y + move[1]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alphas:
                q.add((nx, ny, alphas + board[nx][ny]))
                answer = max(answer, len(alphas) + 1)
    
bfs(0, 0)
print(answer)