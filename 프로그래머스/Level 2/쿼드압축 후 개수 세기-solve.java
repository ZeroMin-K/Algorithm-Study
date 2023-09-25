class Solution {
    private static int[] numbers; 
    
    public int[] solution(int[][] arr) {
        numbers = new int[2];
        int n = arr.length;
        dfs(arr, n, 0, 0, n, n);
        return numbers;
    }
    
    private void dfs(int[][] arr, int n, int startX, int startY, int endX, int endY) {
        int start = arr[startX][startY];
        if (n == 1) {
            numbers[start]++;
            return; 
        }

        boolean compressed = true;
        for (int i = startX; i < endX; i++) {
            for (int j = startY; j < endY; j++) {
                if (start != arr[i][j]) {
                    compressed = false;
                    break; 
                }
            }
        }
        
        if (compressed) { numbers[start]++;} 
        else {
            n /= 2;
            dfs(arr, n, startX, startY, startX + n, startY + n);
            dfs(arr, n, startX, startY + n, startX + n, endY);
            dfs(arr, n, startX + n, startY, endX, startY + n);
            dfs(arr, n, startX + n, startY + n, endX, endY);
        }
    }
}