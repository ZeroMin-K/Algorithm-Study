import java.util.Stack; 

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>(); 
        int i = 0; 
        
        while (i < arr.length) {
            if (stk.empty() || stk.peek() < arr[i]) {
                stk.push(arr[i]);
                i++; 
            } else if (stk.peek() >= arr[i]) {
                stk.pop(); 
            }
        }
        
        int[] answer = new int[stk.size()];
        for (int k = 0; k < answer.length; k++) {
            answer[answer.length - 1 - k] = stk.pop(); 
        }
        
        return answer;
    }
}