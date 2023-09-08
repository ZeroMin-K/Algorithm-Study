import java.util.List;
import java.util.ArrayList;

class Solution {
    private static final int[][] nears = new int[][]{{0, 1}, {1, 0}, {1, 1}};
    public int solution(int m, int n, String[] board) {
        String[][] newBoard = new String[m][n];
        int removedBlockNum = 0;
        boolean isFound = true;
        
        copyBoard(board, newBoard);
        
        while (isFound) {
            isFound = false;
            List<int[]> removedBlocks = new ArrayList<>();
            List<int[]> foundBlocks;
            
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (newBoard[i][j].equals("0")) continue;
                    
                    foundBlocks = findBlocks(i, j, newBoard);
                    if (!foundBlocks.isEmpty()) {
                        isFound = true;
                        removedBlocks.addAll(foundBlocks);
                    }
                }
            }
            
            if (!isFound) break;
            
            removedBlockNum += removeBlocks(removedBlocks, newBoard);
            
            fallBlocks(m, n, newBoard);
        }
        
        return removedBlockNum;
    }
    
    private void copyBoard(String[] source, String[][] dest) {
        for (int i = 0; i < source.length; i++) {
            destination[i] = source[i].split("");
        }
    }
    
    private List<int[]> findBlocks(int x, int y, String[][] board) {
        List<int[]> sameBlocks = new ArrayList<>();
        int m = board.length;
        int n = board[0].length;
        
        sameBlocks.add(new int[]{x, y});
        
        for (int i = 0; i < nears.length; i++) {
            int nx = x + nears[i][0];
            int ny = y + nears[i][1];
            
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || 
               !board[x][y].equals(board[nx][ny]))
                return new ArrayList<int[]>();
            else if (board[x][y].equals(board[nx][ny])) 
                sameBlocks.add(new int[]{nx, ny});
        }
        
        return sameBlocks;
    }
    
    private int removeBlocks(List<int[]> removedBlocks, String[][] board) {
        int m = board.length;
        int n = board[0].length; 
        int removedBlockNum = 0;
        int emptyNum = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j].equals("0")) emptyNum++;
            }
        }
        
        
        for (int[] block : removedBlocks) {
            board[block[0]][block[1]] = "0";
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j].equals("0")) removedBlockNum++;
            }
        }
        
        return removedBlockNum - emptyNum;
    }
    
    private void fallBlocks(int m, int n, String[][] board) {
        for (int j = 0; j < n; j++) {
            for (int i = m - 1; i > 0; i--) {
                int prev = i - 1;
                while (prev >= 0 && board[i][j].equals("0")) {
                    board[i][j] = board[prev][j];
                    board[prev][j] = "0";
                    prev--;
                }
            }
        }
    }
}