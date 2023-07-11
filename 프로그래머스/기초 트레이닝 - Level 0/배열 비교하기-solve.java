import java.util.Arrays;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        int sumArr1;
        int sumArr2; 
        
        if (arr1.length > arr2.length) {
            answer = 1;
        } else if (arr1.length < arr2.length) {
            answer = -1;
        } else {
            sumArr1 = Arrays.stream(arr1).sum();
            sumArr2 = Arrays.stream(arr2).sum();
            
            if (sumArr1 > sumArr2) {
                answer = 1;
            } else if (sumArr1 < sumArr2) {
                answer = -1;
            }
        }
        
        return answer;
    }
}