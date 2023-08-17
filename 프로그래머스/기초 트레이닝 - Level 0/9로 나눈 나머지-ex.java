class Solution {
    public int solution(String number) {
        int answer = 0;
        int length = number.length();
        
        for (int i = 0; i < length; i++) {
            answer += number.charAt(i) - '0';
        }
        
        answer %= 9;
        
        return answer;
    }
}