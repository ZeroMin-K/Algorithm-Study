import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String myStr) {
        String[] answer = new String[]{"EMPTY"};
        List<String> newStrs = new ArrayList<>();
        String newStr = myStr.replace("a", " ").replace("b", " ").replace("c", " ");
        for (String str : newStr.split(" ")) {
            if (str.length() > 0) newStrs.add(str);
        }
        
        if (!newStrs.isEmpty()) answer = newStrs.stream().toArray(String[]::new);
        
        return answer;
    }
}