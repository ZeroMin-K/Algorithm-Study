class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[arr.length];
        int temp;
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = arr[i]; 
        }
        
        for (int[] query : queries) {
            temp = answer[query[0]];
            answer[query[0]] = answer[query[1]];
            answer[query[1]] = temp;
        }
        
        return answer;
    }
}