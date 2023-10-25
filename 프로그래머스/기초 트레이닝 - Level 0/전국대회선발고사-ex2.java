import java.util.Map;
import java.util.List;
import java.util.TreeMap;
import java.util.ArrayList; 

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        Map<Integer, Integer> treeMap = new TreeMap<>();
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) treeMap.put(rank[i], i); 
        }
        
        List<Integer> list = new ArrayList<>();
        for (Integer key : treeMap.keySet()) {
            if (list.size() == 3) break;
            list.add(treeMap.get(key));
        }
        
        return list.get(0) * 10000 + list.get(1) * 100 + list.get(2); 
    }
}