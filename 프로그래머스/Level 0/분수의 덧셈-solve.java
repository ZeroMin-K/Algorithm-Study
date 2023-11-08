class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int resNumer = numer1 * denom2 + numer2 * denom1;
        int resDenom = denom1 * denom2;
        
        for (int div = Math.min(resNumer, resDenom); div >= 2; div--) {
            if (resNumer % div == 0 && resDenom % div == 0) {
                resNumer /= div;
                resDenom /= div;
            }
        }
        
        return new int[] {resNumer, resDenom};
    }
}