class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 1;
        int prefixLength = is_prefix.length();
        int stringLength = my_string.length(); 
        
        if (prefixLength > stringLength) {
            return 0; 
        }
        
        for (int i = 0; i < prefixLength; i++) {
            if (my_string.charAt(i) != is_prefix.charAt(i)) {
                answer = 0; 
            }
        }
        
        
        return answer;
    }
}