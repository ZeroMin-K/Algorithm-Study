import java.util.List;
import java.util.ArrayList;

class Solution {
    private static final int INF = 1000001;
    
    public int[] solution(int[] arr, int[][] queries) {
        List<Integer> answer = new ArrayList<>(); 
        for(int[] query : queries) {
            int minNum = INF; 
            for (int i = query[0]; i <= query[1]; i++) {
                if (arr[i] > query[2]) minNum = Math.min(minNum, arr[i]); 
            }
            answer.add(minNum != INF ? minNum : -1);
        }
        
        return answer.stream().mapToInt(i -> i).toArray(); 
    }
}