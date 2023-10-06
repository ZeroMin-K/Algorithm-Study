import java.util.Stack; 

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>(); 
        int i = 0; 
        
        while ( i < arr.length) {
            if (stk.isEmpty()) {
                stk.push(arr[i]);
                i++;
            } else {
                if (stk.peek() < arr[i]) {
                    stk.push(arr[i]);
                    i++; 
                } else {
                    stk.pop(); 
                }
            }
        }
        
        int[] answer = new int[stk.size()];
        for (int k = answer.length - 1; k >= 0; k--) {
            answer[k] = stk.pop(); 
        }
        
        return answer;
    }
}