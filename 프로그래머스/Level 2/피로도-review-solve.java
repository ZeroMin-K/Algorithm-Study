class Solution {
    
    private static int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        dfs(k, 0, dungeons, visited);
        return answer;
    }
    
    private static void dfs(int k, int now_dungeon, int[][] dungeons, boolean[] visited) {
        if (now_dungeon > answer) {
            answer = now_dungeon;
        }
        
        for (int i = 0; i < dungeons.length; i++) {
            if ((k >= dungeons[i][0]) && !visited[i]) {
                visited[i] = true;
                dfs(k - dungeons[i][1], now_dungeon + 1, dungeons, visited);
                visited[i] = false;
            }
        }
        
    }
}