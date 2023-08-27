import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < intervals.length; i++) {
            for (int k = intervals[i][0]; k <= intervals[i][1]; k++) list.add(arr[k]);
        }
        return list.stream().mapToInt(i -> i).toArray();
    }
}