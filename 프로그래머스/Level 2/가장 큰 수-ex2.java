import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        List<String> list = new ArrayList<>();
        for (int i = 0 ; i < numbers.length; i++) {
            list.add(String.valueOf(numbers[i]));
        }
        
        Collections.sort(list, (a, b) -> {
            return -Integer.compare(Integer.parseInt(a + b), Integer.parseInt(b + a));
        });
        
        StringBuilder sb = new StringBuilder();
        for (String num : list) sb.append(num);
        
        answer = sb.toString();
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}