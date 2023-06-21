class Solution {
    public String solution(String s) {
        StringBuilder string = new StringBuilder(); 
        boolean first = true; 
        char nowChr; 
        for (char chr : s.toCharArray()) {
            nowChr = chr;
            if (chr == ' ') {
                first = true; 
            }
            else if (Character.isAlphabetic(chr)) {
                if (first == true) {
                    nowChr = Character.toUpperCase(chr); 
                    first = false; 
                } else {
                    nowChr = Character.toLowerCase(chr);
                }
            } else {
                first = false; 
            }
            
            string.append(nowChr); 
        }
        
        return string.toString();
    }
}