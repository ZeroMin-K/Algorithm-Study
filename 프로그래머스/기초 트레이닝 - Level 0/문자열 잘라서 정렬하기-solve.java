import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String myString) {
        List<String> list = new ArrayList<>();
        for (String word : myString.split("x")){
            if (word.length() > 0) {
                list.add(word);
            }
        }
        
        return list.stream()
                    .sorted()
                    .toArray(String[]::new);
    }
}