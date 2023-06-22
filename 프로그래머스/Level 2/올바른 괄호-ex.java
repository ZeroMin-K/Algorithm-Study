import java.util.Stack; 

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int length = s.length(); 
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < length; i++) {
            if (s.charAt(i) == '(') {
                stack.push(1);
            } else {
                if (stack.isEmpty()) {
                    answer = false;
                    break;
                } else {
                    stack.pop();
                }
            }
        }
        
        if (! stack.isEmpty()) {
            answer = false;
        }


        return answer;
    }
}