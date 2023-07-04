import java.util.Stack; 

class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack = new Stack<>();
        
        for (char alpha : s.toCharArray()) {
            if (stack.size() > 0 && stack.peek() == alpha) {
                stack.pop();
            } else {
                stack.push(alpha);
            }
        }

        return stack.size() == 0 ? 1 : 0;
    }
}