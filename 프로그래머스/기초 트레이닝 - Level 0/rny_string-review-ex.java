class Solution {
    public String solution(String rny_string) {
        StringBuilder stringBuilder = new StringBuilder();
        
        for (int i = 0; i < rny_string.length(); i++) {
            String str = String.valueOf(rny_string.charAt(i));
            
            if (str.equals("m")) {
                str = "rn";
            }
            
            stringBuilder.append(str);
        }
        return stringBuilder.toString();
    }
}