class Solution {
    public String solution(String cipher, int code) {
        String answer = "";
        
        int len = cipher.length();
        
        for (int i = code - 1; i < len; i += code) {
            answer = answer + cipher.charAt(i);
        }
        
        return answer;
    }
}