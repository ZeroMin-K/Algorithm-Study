class Solution {
    public int solution(String myString, String pat) {
        StringBuilder sb = new StringBuilder();
        
        for (String str : myString.split("")) {
            if (str.equals("A")) {
                sb.append("B");
            } else if (str.equals("B")) {
                sb.append("A");
            } else {
                sb.append(str); 
            }
        }
        return sb.toString().contains(pat) ? 1 : 0; 
    }
}