class Solution {
    public int[] solution(int n, int k) {
        int length = n / k;
        
        int[] answer = new int[length];
        
        for (int i = 1; i <= length; i++) {
            answer[i - 1] = k * i;
        }
        
        return answer;
    }
}