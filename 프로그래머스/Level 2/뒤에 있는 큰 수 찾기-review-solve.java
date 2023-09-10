import java.util.Stack;

class Solution {
    public int[] solution(int[] numbers) {
        int[] bigNums = new int[numbers.length];
        Stack<int[]> stack = new Stack<>();
        
        for (int i = 0; i < numbers.length; i++) {
            while (!stack.isEmpty() && stack.peek()[1] < numbers[i]) {
                int[] elem = stack.pop();
                bigNums[elem[0]] = numbers[i];
                
            }
            stack.push(new int[] {i, numbers[i]});
        }
        
        while (!stack.isEmpty()) {
            int[] elem = stack.pop();
            bigNums[elem[0]] = -1;
        }
        
        return bigNums;
    }
}