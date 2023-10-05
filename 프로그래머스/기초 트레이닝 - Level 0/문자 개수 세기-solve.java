import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(String my_string) {
        List<Integer> alphas = new ArrayList<>();
        int[][] alphaRanges = new int[][]{{(int) 'A', (int)'Z' + 1}, {(int) 'a', (int) 'z' + 1}};
        int length = my_string.length(); 
        
        for (int[] alphaRange : alphaRanges) {
            for (int k = alphaRange[0]; k < alphaRange[1]; k++) {
                char alpha = (char) k; 
                int count = 0;
                for (int i = 0; i < length; i++) {
                    if (my_string.charAt(i) == alpha) count++;
                }
                alphas.add(count); 
            }
        }
        
        return alphas.stream().mapToInt(i -> i).toArray();
    }
}