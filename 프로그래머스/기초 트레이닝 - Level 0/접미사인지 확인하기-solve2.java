class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 1; 
        int suffixLength = is_suffix.length();
        int stringLength = my_string.length();
        
        if (suffixLength > stringLength) {
            return 0;
        }
        
        int idx = 0;
        for (int i = stringLength - suffixLength; i < stringLength; i++) {
            if (my_string.charAt(i) != is_suffix.charAt(idx++)) {
                answer = 0; 
            }
        }
        
        return answer; 
    }
}