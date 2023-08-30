class Solution {
    int solution(int[][] land) {
        int n = land.length;
        int cols = land[0].length;
        int max = 0; 
        int[][] dp = new int[n][cols];
        
        for (int j = 0; j < cols; j++) {
            dp[0][j] = land[0][j]; 
        }
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < cols; j++) {
                for (int k = 0; k < cols; k++) {
                    if (k != j) max = Math.max(max, dp[i - 1][k]);
                }
                dp[i][j] = max + land[i][j];
                max = 0; 
            }
        }
        
        
        for (int score : dp[n - 1]) max = Math.max(max, score);

        return max;
    }
}