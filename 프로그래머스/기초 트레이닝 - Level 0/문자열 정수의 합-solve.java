class Solution {
    public int solution(String num_str) {
        int answer = 0;
        int length = num_str.length();
        
        for (int i = 0; i < length; i++) {
            answer += Character.getNumericValue(num_str.charAt(i));
        }
        
        return answer;
    }
}