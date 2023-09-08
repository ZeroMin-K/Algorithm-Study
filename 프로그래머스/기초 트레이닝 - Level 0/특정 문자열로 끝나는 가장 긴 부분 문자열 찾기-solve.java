class Solution {
    public String solution(String myString, String pat) {
        int length = myString.length(); 
        int n = 0;
        for (int i = 1; i <= length; i++) {
            if (myString.substring(0, i).endsWith(pat)) n = Math.max(n, i);
        }
        return myString.substring(0, n);
    }
}