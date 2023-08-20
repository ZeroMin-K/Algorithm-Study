import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String myString) {
        String[] answer = {};
        List<String> myStrings = new ArrayList<>();
        
        for (String word : myString.split("x")) {
            if (word.length() > 0) {
                myStrings.add(word);
            }
        }
        
        return myStrings.stream().sorted().toArray(String[]::new);
    }
}