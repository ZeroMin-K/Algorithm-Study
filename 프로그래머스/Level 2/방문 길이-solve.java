import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

class Solution {
    public int solution(String dirs) {
        Map<String, int[]> moves = new HashMap<>();
        Set<String> paths = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        int[] path1; 
        int[] path2;
        int x = 0;
        int y = 0; 
        int nx;
        int ny;
        
        moves.put("U", new int[] {-1, 0});
        moves.put("D", new int[] {1, 0});
        moves.put("R", new int[] {0, 1});
        moves.put("L", new int[] {0, -1});
        
        for (String dir : dirs.split("")) {
            nx = x + moves.get(dir)[0];
            ny = y + moves.get(dir)[1];
            
            if (-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5) {
                path1 = new int[]{x, y, nx, ny};
                path2 = new int[]{nx, ny, x, y};
                
                for (int loc : path1) sb.append(Integer.toString(loc));
                paths.add(sb.toString());
                sb.setLength(0);
                
                for (int loc : path2) sb.append(Integer.toString(loc));
                paths.add(sb.toString());
                sb.setLength(0);
                
                x = nx;
                y = ny; 
            }
        }
        
        return (int) paths.size() / 2;
    }
}