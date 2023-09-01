import java.util.Arrays;

class Solution {
    public String solution(String my_string, int[] indices) {
        StringBuilder answer = new StringBuilder();
        int length = my_string.length();
        int index = 0;
        
        Arrays.sort(indices);
        
        for (int i = 0; i < length; i++) {
            if (index < indices.length && i == indices[index]) {
                index++;
            } else {
                answer.append(my_string.charAt(i));
            }
        }
        
        return answer.toString();
    }
}