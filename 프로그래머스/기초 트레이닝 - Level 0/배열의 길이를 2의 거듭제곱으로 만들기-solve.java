import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int elem : arr) list.add(elem);
        
        int n = 0; 
        int size = list.size();
        
        while (size > Math.pow(2, n)) n++;
        
        for (int i = 0; i < Math.pow(2, n) - size; i++) list.add(0);
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}