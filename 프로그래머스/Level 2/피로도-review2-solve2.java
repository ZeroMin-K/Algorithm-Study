class Solution {
    public int solution(int k, int[][] dungeons) {
        int maxCompletedDungeonsNum = dfs(k, 0, dungeons, 
																					new boolean[dungeons.length]);
        return maxCompletedDungeonsNum;
    }
    
    private int dfs(int nowFatigue, int completedDungeons, 
										int[][] dungeons, boolean[] visited) {
        int maxCompletedDungeonsNum = completedDungeons;
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && nowFatigue >= dungeons[i][0]) {
                visited[i] = true;
                int result = dfs(nowFatigue - dungeons[i][1], 
																	completedDungeons + 1, dungeons, visited);
                maxCompletedDungeonsNum = 
																		Math.max(maxCompletedDungeonsNum, result);
                visited[i] = false;
            }
        }
        
        return maxCompletedDungeonsNum;
    }
}