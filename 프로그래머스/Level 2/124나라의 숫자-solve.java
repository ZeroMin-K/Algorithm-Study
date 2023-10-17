class Solution {
    public String solution(int n) {
        StringBuilder convertedNum = new StringBuilder(); 
        String[] digits = new String[]{"1", "2", "4"};
        
        while (n > 0) {
            n--;
            convertedNum.append(digits[n % 3]);
            n /= 3;
        }
        
        return convertedNum.reverse().toString();
    }
}