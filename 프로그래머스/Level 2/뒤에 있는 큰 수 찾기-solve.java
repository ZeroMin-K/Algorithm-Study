import java.util.Stack;

class Solution {
    public int[] solution(int[] numbers) {
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[numbers.length];
        for (int i = 0; i < answer.length; i++) answer[i] = -1;
        
        for (int i = 0; i < numbers.length; i++) {
            while (!stack.isEmpty() && numbers[stack.peek()] < numbers[i]) 
                answer[stack.pop()] = numbers[i];
            stack.push(i);
        }
        
        return answer;
    }
}