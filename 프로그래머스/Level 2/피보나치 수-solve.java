class Solution {
    public int solution(int n) {
        long[] fiboArr = new long[n + 1];
        fiboArr[1] = 1;
        
        for (int i = 2; i <= n; i++) {
            fiboArr[i] = fiboArr[i - 1] % 1234567 + fiboArr[i - 2] % 1234567;
        }
        
        return (int) fiboArr[n] % 1234567;
    }
}