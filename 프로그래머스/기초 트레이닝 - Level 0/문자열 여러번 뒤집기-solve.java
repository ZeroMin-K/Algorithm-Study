class Solution {
    public String solution(String my_string, int[][] queries) {
        StringBuilder sb = new StringBuilder(); 
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            
            for(int i = 0; i < s; i++) {
                sb.append(my_string.charAt(i));
            }
            
            for (int i = e; i >= s; i--) {
                sb.append(my_string.charAt(i));
            }
            
            for (int i = e + 1; i < my_string.length(); i++) {
                sb.append(my_string.charAt(i));
            }
            
            my_string = sb.toString();
            sb.setLength(0);
        }
        return my_string;
    }
}