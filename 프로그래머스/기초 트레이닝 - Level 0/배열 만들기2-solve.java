import java.util.List;
import java.util.ArrayList; 

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> answer = new ArrayList<>(); 
        
        for (int i = l; i <= r; i++) {
            boolean only5And0 = true;
            for (char num : Integer.toString(i).toCharArray()) {
                if (num != '5' && num != '0') {
                    only5And0 = false;
                    break; 
                }
            }
            
            if (only5And0) answer.add(i);
        }
        
        return !answer.isEmpty() ? answer.stream().mapToInt(i -> i).toArray() : new int[]{-1};
    }
}