import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        List<Integer> list = new ArrayList<>();
        int value;
        long i;
        long j;
        
        for (long k = left; k <= right; k++) {
            i = k / n;
            j = k % n; 
            value = (int) Math.max(i, j) + 1;
            list.add(value);
        }
        
        return list.stream()
                    .mapToInt(num -> num)
                    .toArray();
    }
}