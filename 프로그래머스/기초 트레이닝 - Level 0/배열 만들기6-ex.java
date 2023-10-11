import java.util.Stack;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < arr.length; i++) {
            if (!stack.isEmpty() && stack.peek() == arr[i]) stack.pop();
            else stack.push(arr[i]); 
        }
        
        return stack.isEmpty() ? new int[] {-1} : stack.stream().mapToInt(i -> i).toArray();
    }
}