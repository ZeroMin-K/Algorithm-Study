class Solution {
    public String solution(String str1, String str2) {
        StringBuilder sb = new StringBuilder();
        char[] char1s = str1.toCharArray();
        char[] char2s = str2.toCharArray();
        
        for (int i = 0; i < char1s.length; i++) {
            sb.append(char1s[i]).append(char2s[i]);
        }
        
        return sb.toString();
    }
}