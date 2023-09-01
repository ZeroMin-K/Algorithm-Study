import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        bfs(maps, n, m);
        
        return maps[n - 1][m - 1] > 1 ? maps[n - 1][m - 1] : -1;
    }
    
    private static void bfs(int[][] maps, int n, int m) {
        Queue<int[]> queue = new LinkedList<>();
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        queue.add(new int[]{0, 0});
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int nextDist = maps[x][y] + 1; 
            
            for (int[] direction : directions) {
                int nx = x + direction[0];
                int ny = y + direction[1];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] == 1) {
                    maps[nx][ny] = nextDist;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }
}