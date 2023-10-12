class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] arr = my_string.toCharArray(); 
        
        for (int[] query: queries) {
            arr = reverseArr(arr, query[0], query[1]);
        }
        
        StringBuilder sb = new StringBuilder();
        for(char elem : arr) sb.append(elem); 
        
        return sb.toString();
    }
    
    private char[] reverseArr(char[] arr, int s, int e) {
        while (s < e) {
            char temp = arr[s];
            arr[s++] = arr[e];
            arr[e--] = temp; 
        }
        
        return arr; 
    }
}