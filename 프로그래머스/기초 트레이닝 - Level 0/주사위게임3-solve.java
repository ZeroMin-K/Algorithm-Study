import java.util.Arrays;
import java.util.List;
import java.util.ArrayList; 

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] diceResults = new int[] {a, b, c, d};
        int[] diceCounts = new int[7];
        for (int dice : diceResults) {
            diceCounts[dice]++; 
        }
        
        List<Integer>[] diceCountsToDices = new ArrayList[5]; 
        for (int i = 0; i < diceCountsToDices.length; i++) {
            diceCountsToDices[i] = new ArrayList<>(); 
        }
        
        for (int i = 1; i < diceCounts.length; i++) {
            diceCountsToDices[diceCounts[i]].add(i);
        }
        
        Arrays.sort(diceResults); 
        int answer = diceResults[0]; 
        
        if (!diceCountsToDices[4].isEmpty()) {
            answer = 1111 * diceCountsToDices[4].get(0);
        } else if (!diceCountsToDices[3].isEmpty()) {
            answer = (int) Math.pow(10 * diceCountsToDices[3].get(0) 
                                    + diceCountsToDices[1].get(0), 2);
        } else if (!diceCountsToDices[2].isEmpty()) {
            int p = diceCountsToDices[2].get(0);
            int q; 
            if (!diceCountsToDices[1].isEmpty()) {
                q = diceCountsToDices[1].get(0);
                int r = diceCountsToDices[1].get(1); 
                answer = q * r; 
            } else {
                q = diceCountsToDices[2].get(1);
                answer = (p + q) * Math.abs(p - q); 
            }
        }
        
        return answer;
    }
}