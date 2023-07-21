import java.util.*;

class Solution {
    public int solution(int[] elements) {
        Set<Integer> set = new HashSet<>();
        int sum; 
        
        for (int length = 1; length <= elements.length; length++) {
            for (int start = 0; start < elements.length; start++) {
                sum = 0; 
                for(int k = start; k < start + length; k++) {
                    sum += elements[k % elements.length];
                }
                set.add(sum);
            }
        }
        
        return set.size();
    }
}