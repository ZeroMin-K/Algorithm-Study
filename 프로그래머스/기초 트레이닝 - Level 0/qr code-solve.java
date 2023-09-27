class Solution {
    public String solution(int q, int r, String code) {
        StringBuilder sb = new StringBuilder();
        int length = code.length(); 
        
        for (int i = 0; i < length; i++) {
            if (i % q == r) sb.append(code.charAt(i));
        }
        return sb.toString();
    }
}