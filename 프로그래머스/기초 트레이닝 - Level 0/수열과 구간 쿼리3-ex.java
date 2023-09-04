import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        int i; 
        int j;
        int temp; 
        
        for (int[] query : queries) {
            i = query[0];
            j = query[1];
            temp = answer[i];
            
            answer[i] = answer[j];
            answer[j] = temp; 
        }
        
        return answer;
    }
}