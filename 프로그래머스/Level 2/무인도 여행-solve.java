import java.util.Queue; 
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Collections; 

class Solution {
    private static final int[][] moves = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; 
    
    public int[] solution(String[] maps) {
        List<Integer> stays = new ArrayList<>();
        int n = maps.length;
        int m = maps[0].length(); 
        
        boolean[][] visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = false; 
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) != 'X' && !visited[i][j]) {
                    int stay = bfs(maps, visited, i, j);
                    stays.add(stay);
                }
            }
        }
        
        if (stays.isEmpty()) stays.add(-1);
        Collections.sort(stays);
        
        return stays.stream().mapToInt(i -> i).toArray(); 
    }
    
    private int bfs(String[] maps, boolean[][] visited, int startX, int startY) {
        int n = maps.length;
        int m = maps[0].length();
        int stay = Character.getNumericValue(maps[startX].charAt(startY));
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{startX, startY});
        visited[startX][startY] = true; 
        
        while (!q.isEmpty()) {
            int[] next = q.poll();
            
            for (int[] move : moves) {
                int nx = next[0] + move[0];
                int ny = next[1] + move[1];
                
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                
                if (maps[nx].charAt(ny) != 'X' && !visited[nx][ny]) {
                    stay += Character.getNumericValue(maps[nx].charAt(ny));
                    q.add(new int[]{nx, ny});
                    visited[nx][ny] = true; 
                }
            }
        }
        
        return stay; 
    }
}