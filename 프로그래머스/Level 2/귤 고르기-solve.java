import java.util.Arrays;

class Solution {
    public int solution(int k, int[] tangerines) {
        int total = 0;
        int minTypes = 0;
        
        Arrays.sort(tangerines);
        int[] tangerinesNums = new int[tangerines[tangerines.length - 1] + 1];
        
        for (int tangerine : tangerines) {
            tangerinesNums[tangerine]++;
        }
        
        Arrays.sort(tangerinesNums);
        
        for (int i = tangerinesNums.length - 1; i >= 0; i--) {
            total += tangerinesNums[i];
            minTypes++;
            
            if (total >= k) {
                break;
            }
            
        }
        
        return minTypes;
    }
}