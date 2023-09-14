class Solution {
    public int[] solution(int[] arr) {
        int len = arr.length;
        int temp = 1;
        
        while (temp < len) {
            temp *= 2;
        }
        
        int[] answer = new int[temp];
        
        for (int i = 0; i < arr.length; i++) {
            answer[i] = arr[i];
        }
        
        return answer;
    }
}