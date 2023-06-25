import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = Arrays.copyOf(num_list, num_list.length + 1);
        
        if (num_list[num_list.length - 1] > num_list[num_list.length -2]) {
            answer[answer.length - 1] = num_list[num_list.length - 1]  - num_list[num_list.length - 2]; 
        } else {
            answer[answer.length - 1] = 2 * num_list[num_list.length - 1];
        }
        
        return answer;
    }
}