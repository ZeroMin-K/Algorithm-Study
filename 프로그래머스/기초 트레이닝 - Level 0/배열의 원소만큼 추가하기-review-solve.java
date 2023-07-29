import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int num : arr) {
            for (int i = 0 ; i < num; i++) {
                list.add(num);
            }
        }
        
        return list.stream()
                    .mapToInt(i -> i)
                    .toArray();
    }
}