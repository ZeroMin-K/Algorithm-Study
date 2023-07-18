class Solution {
    public String solution(String myString) {
        int length = myString.length();
        int lAsc = (int) 'l'; 
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < length; i++) {
            if ((int) myString.charAt(i) < lAsc) {
                sb.append("l");
            } else {
                sb.append(String.valueOf(myString.charAt(i)));
            }
        }
        
        return sb.toString();
    }
}