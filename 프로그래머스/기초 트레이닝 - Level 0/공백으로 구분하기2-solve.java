import java.util.ArrayList;

class Solution {
    public String[] solution(String my_string) {
        ArrayList<String> list = new ArrayList<>();
        
        for (String str: my_string.split(" ")) {
            if (!str.equals(" ") && !str.equals("")) {
                list.add(str);
            }
        }
        
        return list.toArray(new String[0]);
    }
}