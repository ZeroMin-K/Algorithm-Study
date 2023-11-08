class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer;
        
        int resDenom = denom1 * denom2;
        int resNumer = denom1 * numer2 + denom2 * numer1;
        
        answer = new int[]{resNumer, resDenom};
        
        int gcd = getGcd(answer[0], answer[1]);
        answer[0] /= gcd;
        answer[1] /= gcd;
        
        return answer;
    }
    
    private int getGcd(int num1, int num2) {
        if (num1 % num2 == 0) return num2;
        return getGcd(num2, num1 % num2); 
    }
}