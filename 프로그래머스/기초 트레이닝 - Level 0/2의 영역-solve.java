import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        boolean is2In = false;
        int start = 0;
        int end = arr.length - 1;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                start = i;
                is2In = true;
                break; 
            }
        }
        
        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == 2) {
                end = i;
                break; 
            }
        }
        
        return is2In ? Arrays.copyOfRange(arr, start, end + 1) : new int[]{-1};
    }
}