def solution(n):
    dirs = {0 : (1, 0), 1 : (0, 1), 2 : (-1, -1)}
    
    tri = [[0] * i for i in range(1, n + 1)]
    x, y, num = -1, 0, 1
    for i in range(n):
        for _ in range(i, n):
            x, y = x + dirs[i % 3][0], y + dirs[i % 3][1]
            tri[x][y] = num
            num += 1
    
    answer = [] 
    for i in range(n):
        for j in range(len(tri[i])):
            answer.append(tri[i][j])
    
    return answer