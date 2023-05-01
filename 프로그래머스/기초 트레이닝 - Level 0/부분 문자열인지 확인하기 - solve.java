class Solution {
    public int solution(String my_string, String target) {
        int answer = 0;
        int patternLength = my_string.length();
        int targetLength = target.length();
        
        for (int i = 0; i < patternLength - targetLength; i++) {
            if (my_string.substring(i, i + targetLength).equals(target)) {
                answer = 1;
            }
        }
        return answer;
    }
}