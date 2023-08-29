import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> list = new ArrayList<>();
        int num; 
        
        for (String intStr : intStrs) {
            num = Integer.parseInt(intStr.substring(s, s + l));
            if (num > k) list.add(num);
        }
        
        return list.stream().mapToInt(i -> i).toArray();
    }
}