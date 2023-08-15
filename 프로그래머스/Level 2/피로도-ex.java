class Solution {
    public static boolean visited[];
    public static int answer = 0;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        
        dfs(k, dungeons, 0);
        
        return answer;
    }
    
    public static void dfs(int tired, int[][] dungeons, int count) {
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && dungeons[i][0] <= tired) {
                visited[i] = true;
                dfs(tired - dungeons[i][1], dungeons, count + 1);
                visited[i] = false;
            }
        }
        
        answer = Math.max(answer, count);
    }
}