import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String my_string) {
        StringBuilder stringBuilder; 
        List<String> stringList = new ArrayList<>();
        String[] myStringArr = my_string.split("");
        
        for (int i = 0; i < myStringArr.length; i++) {
            stringBuilder = new StringBuilder();
            for(int start = i; start < myStringArr.length; start++) {
                stringBuilder.append(myStringArr[start]);
            }
            stringList.add(stringBuilder.toString());
        }
        
        return stringList.stream()
                        .sorted()
                        .toArray(String[]::new);
            
    }
}