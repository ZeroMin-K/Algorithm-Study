def solution(dirs):
    moves = {'U' : (-1, 0), 'D' : (1, 0), 'R' : (0, 1), 'L' : (0, -1)}
    paths = set() 
    x, y = 0, 0
    for dir in dirs: 
        nx, ny = x + moves[dir][0], y + moves[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            paths.add((x, y, nx, ny))
            paths.add((nx, ny, x, y))
            x, y = nx, ny 
            
    return len(paths) // 2