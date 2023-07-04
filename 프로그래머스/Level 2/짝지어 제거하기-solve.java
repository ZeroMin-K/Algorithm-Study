import java.util.Stack;

class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack = new Stack<>();
        int length = s.length(); 
        stack.push(s.charAt(0));
        
        for (int i = 1; i < length; i++) {
            if (stack.size() > 0 && stack.peek() == s.charAt(i)) {
                stack.pop();
            } else {
                stack.push(s.charAt(i));
            }
        }

        return (stack.size() == 0) ? 1 : 0;
    }
}