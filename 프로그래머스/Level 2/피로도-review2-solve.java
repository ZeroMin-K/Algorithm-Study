import java.util.Arrays;

class Solution {
    private static int maxCompletedDungeonsNum;
    
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        maxCompletedDungeonsNum = 0;
        Arrays.fill(visited, false);
        
        dfs(k, 0, visited, dungeons);
        return maxCompletedDungeonsNum;
    }
    
    private void dfs(int nowFatigue, int completedDungeons, boolean[] visited, int[][] dungeons) {
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && nowFatigue >= dungeons[i][0]) {
                visited[i] = true;
                dfs(nowFatigue - dungeons[i][1], completedDungeons + 1, visited, dungeons);
                visited[i] = false;
            }
        }
        
        maxCompletedDungeonsNum = Math.max(maxCompletedDungeonsNum, completedDungeons);
    }
}