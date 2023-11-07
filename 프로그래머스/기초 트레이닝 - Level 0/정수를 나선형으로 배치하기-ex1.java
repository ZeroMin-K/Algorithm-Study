class Solution {
    public int[][] solution(int n) {
        int[][] array = new int[n][n];
        int num = 1;
        int rowStart = 0, rowEnd = n - 1;
        int colStart = 0, colEnd = n - 1;
        
        while (rowStart <= rowEnd && colStart <= colEnd) {
            for (int i = colStart; i <= colEnd; i++) {
                array[rowStart][i] = num++;
            }
            rowStart++;
            
            for (int i = rowStart; i <= rowEnd; i++) {
                array[i][colEnd] = num++; 
            }
            colEnd--;
            
            for (int i = colEnd; i >= colStart; i--) {
                array[rowEnd][i] = num++; 
            }
            rowEnd--;
            
            for(int i = rowEnd; i>= rowStart; i--) {
                array[i][colStart] = num++; 
            }
            colStart++;
        }
        
        
        return array;
    }
}