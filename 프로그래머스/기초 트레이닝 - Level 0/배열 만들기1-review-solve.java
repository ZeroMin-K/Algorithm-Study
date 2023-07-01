class Solution {
    public int[] solution(int n, int k) {
        int[] answer = new int[n / k];
        answer[0] = k; 
        for (int i = 1; i < answer.length; i++) {
            answer[i] = answer[i - 1] + k;
        }
        return answer;
    }
}