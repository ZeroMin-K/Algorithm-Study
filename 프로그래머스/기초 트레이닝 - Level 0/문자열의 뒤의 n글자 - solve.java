class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        int length = my_string.length();
        
        for (int i = length - n; i < length; i++) {
            answer += my_string.charAt(i);
        }
        
        return answer;
    }
}