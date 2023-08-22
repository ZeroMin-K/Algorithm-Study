class Solution {
    public String solution(String str1, String str2) {
        StringBuilder sb = new StringBuilder();
        String[] str1s = str1.split("");
        String[] str2s = str2.split("");
        
        for (int i = 0; i < str1s.length; i++) {
            sb.append(str1s[i]).append(str2s[i]);
        }
        
        return sb.toString();
    }
}