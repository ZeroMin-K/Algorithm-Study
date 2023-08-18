import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> list = new ArrayList<>();
        
        for (int k = 0; k < 2; k++) {
            for (int i = intervals[k][0]; i <= intervals[k][1]; i++) {
                list.add(arr[i]);
            }
        }
        
        return list.stream()
                    .mapToInt(i -> i)
                    .toArray();
    }
}