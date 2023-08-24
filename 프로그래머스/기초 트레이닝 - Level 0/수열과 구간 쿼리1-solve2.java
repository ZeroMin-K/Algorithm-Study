class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[arr.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = arr[i];
        }
        
        for (int[] query : queries) {
            for (int i = query[0]; i <= query[1]; i++) {
                answer[i]++;
            }
        }
        
        return answer;
    }
}