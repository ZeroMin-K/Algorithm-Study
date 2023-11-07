class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int[][] moves = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int num = 2, end = n * n; 
        int x = 0, y = 0, dir = 0;
        answer[x][y] = 1;
        
        while (num <= end) {
            int nx = x + moves[dir][0], ny = y + moves[dir][1];
            
            if (0 <= nx && nx < n && 0 <= ny && ny < n && answer[nx][ny] == 0) {
                answer[nx][ny] = num++;
                x = nx; y = ny; 
            } else {
                dir = (dir + 1) % moves.length;
            }
        }
        
        return answer;
    }
}