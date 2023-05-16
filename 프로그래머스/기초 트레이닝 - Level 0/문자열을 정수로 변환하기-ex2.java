class Solution {
    public int solution(String n_str) {
        int answer = 0;
        int strLength = n_str.length();
        
        for (int i = 0; i < strLength; i++) {
            answer = answer * 10;
            answer += n_str.charAt(i) - 48;
        }
        
        return answer;
    }
}