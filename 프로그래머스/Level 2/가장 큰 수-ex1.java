import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String solution(int[] numbers) {
        String[] strNums = new String[numbers.length];
        
        for (int i = 0; i < strNums.length; i++)
            strNums[i] = numbers[i] + "";
        
        Arrays.sort(strNums, new Comparator<String> () {
            public int compare(String o1, String o2) {
                return (o2 + o1).compareTo(o1 + o2);
            }
        });
        
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < strNums.length; i++) answer.append(strNums[i]);
        
        return answer.toString().charAt(0) == '0' ? "0" : answer.toString();
    }
}