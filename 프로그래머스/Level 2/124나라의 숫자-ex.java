class Solution {
    public String solution(int n) {
        String[] digits = {"4", "1", "2"};
        String convertedNum = "";
        
        while (n > 0) {
            convertedNum = digits[n % 3] + convertedNum;
            n = (n - 1) / 3;
        }
        
        return convertedNum;
    }
}