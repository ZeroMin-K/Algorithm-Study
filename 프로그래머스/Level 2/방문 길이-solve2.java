import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(String dirs) {
        Map<String, int[]> moves = new HashMap<>();
        Set<String> paths = new HashSet<>();
        int[] path1; 
        int[] path2;
        int x = 0;
        int y = 0; 
        
        moves.put("U", new int[] {-1, 0});
        moves.put("D", new int[] {1, 0});
        moves.put("R", new int[] {0, 1});
        moves.put("L", new int[] {0, -1});
        
        for (String dir : dirs.split("")) {
            int[] move = moves.get(dir);
            int nx = x + move[0];
            int ny = y + move[1];
            
            if (-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5) {
                String path = getPath(x, y, nx, ny);
                paths.add(path);
                
                path = getPath(nx, ny, x, y);
                paths.add(path);
                
                x = nx;
                y = ny; 
            }
        }
        
        return (int) paths.size() / 2;
    }
    
    private String getPath(int x, int y, int nx, int ny) {
        StringBuilder sb = new StringBuilder();
        sb.append(x).append(y).append(nx).append(ny);
        return sb.toString();
    }
}