import java.util.Arrays; 

class Solution {
    public int solution(int x, int y, int n) {
        int[] dp = new int[y + 1];
        int[][] ops = new int[][]{{1, n}, {2, 0}, {3, 0}};
        int INF = 1000001;
        Arrays.fill(dp, INF);
        dp[x] = 0; 
        for (int k = x; k <= y; k++) {
            for (int[] op : ops) {
                int next = k * op[0] + op[1];
                if (next <= y) dp[next] = Math.min(dp[next], dp[k] + 1);
            }
        }
        
        return dp[y] != INF ? dp[y] : -1;
    }
}