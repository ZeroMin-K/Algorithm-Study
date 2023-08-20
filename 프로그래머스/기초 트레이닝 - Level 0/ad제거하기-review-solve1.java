import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> strings = new ArrayList<>();
        
        for (String word : strArr) {
            if (!word.contains("ad")) {
                strings.add(word);
            }
        }
        
        return strings.stream().toArray(String[]::new);
    }
}