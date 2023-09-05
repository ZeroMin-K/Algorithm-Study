class Solution {
    public String solution(String my_string, int s, int e) {
        StringBuilder sb = new StringBuilder();
        int length = my_string.length();
        
        for (int i = 0; i < s; i++) {
            sb.append(my_string.charAt(i));
        }
        
        for (int i = e; i >= s; i--) {
            sb.append(my_string.charAt(i));
        }
        
        for (int i = e + 1; i < length; i++) {
            sb.append(my_string.charAt(i));
        }
        
        return sb.toString();
    }
}