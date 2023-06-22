import java.util.*;

class Solution {
    public int[] solution(int n, int k) {
        int[] answer = {};
        
        List<Integer> arr = new ArrayList<>();
        
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                arr.add(i);
            }
        }
        
        return arr.stream()
                .mapToInt(i -> i)
                .toArray();
    }
}