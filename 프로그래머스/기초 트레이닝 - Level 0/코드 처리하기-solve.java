class Solution {
    public String solution(String code) {
        StringBuilder sb = new StringBuilder();
        int length = code.length(); 
        int mode = 0; 
        
        for (int i = 0; i < length; i++) {
            if (mode == 0) {
                if (code.charAt(i) != '1') {
                    if (i % 2 == 0) sb.append(code.charAt(i)); 
                } else mode = 1; 
            } else if (mode == 1) {
                if (code.charAt(i) != '1') {
                    if (i % 2 == 1) sb.append(code.charAt(i));
                } else mode = 0; 
            }
        }
        
        return sb.length() > 0 ? sb.toString() : "EMPTY"; 
    }
}