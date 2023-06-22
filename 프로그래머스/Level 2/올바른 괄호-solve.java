class Solution {
    boolean solution(String s) {
        boolean answer;
        
        int total = 0; 
        int length = s.length(); 
        
        for (int i = 0; i < length; i++) {
            if (s.charAt(i) == '(') {
                total += 1;
            } else {
                total -= 1;
                if (total < 0) {
                    return false;
                }
            }
        }
        
        answer = (total == 0) ? true : false; 
        return answer;
    }
}