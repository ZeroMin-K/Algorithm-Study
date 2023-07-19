import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int sLength = s.length();
        String extendedS = s + s;
        
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < sLength; i++) {
            for (int j = i; j < i + sLength; j++) {
                char bracket = extendedS.charAt(j);
                if (bracket =='(' || bracket == '{' || bracket == '[') {
                    stack.push(bracket);
                } else if (stack.size() > 0 && stack.peek() == map.get(bracket)) {
                    stack.pop();
                } else {
                    stack.push(bracket);
                }
            }
         
            
            if (stack.empty()) {
                answer++;
            }
            
            stack.clear();
        }
        
        
        return answer;
    }
}