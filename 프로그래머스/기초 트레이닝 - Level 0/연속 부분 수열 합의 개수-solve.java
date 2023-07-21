import java.util.*;

class Solution {
    public int solution(int[] elements) {
        HashSet<Integer> set = new HashSet<>();
        int[] circleSeq = new int[2 * elements.length];
        int index = 0;
        int sum = 0; 
        
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < elements.length; j++) {
                circleSeq[index++] = elements[j];
            }
        }
        
        for (int length = 1; length <= elements.length; length++) {
            for (int i = 0; i < elements.length; i++) {
                for (int k = i; k < i + length; k++) {
                    sum += circleSeq[k];
                }
                set.add(sum);
                sum = 0; 
            }
        }
        
        return set.size();
    }
}