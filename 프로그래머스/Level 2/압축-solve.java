import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Solution {
    public int[] solution(String msg) {
        List<Integer> compressedIndices = new ArrayList<>();
        Map<String, Integer> indicesMap = new HashMap<>();
        String w;
        int length = msg.length();
        int lastIndex = 27;
        int startIndex = 0;
        
        for (int i = (int)'A'; i <= (int)'Z'; i++) {
            indicesMap.put(Character.toString((char) i), i - (int)'A' + 1);
        }
        
        for (int i = 0; i < length; i++) {
            if (i != startIndex) continue;
            
            for (int j = length; j > i; j--) {
                w = msg.substring(i, j);
                if (indicesMap.containsKey(w)) {
                    compressedIndices.add(indicesMap.get(w));
                    if (j < length - 1) {
                        indicesMap.put(w + msg.charAt(j), lastIndex);
                        lastIndex++;
                    }
                    startIndex = j;
                    break;
                }
            }
        }
        
        return compressedIndices.stream().mapToInt(i -> i).toArray();
    }
}