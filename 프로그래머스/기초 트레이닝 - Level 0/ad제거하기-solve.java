import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> list = new ArrayList<>();
        for (String word: strArr) {
            if (!word.contains("ad")) {
                list.add(word);
            }
        }
        
        return list.stream()
                .toArray(String[]::new);
    }
}