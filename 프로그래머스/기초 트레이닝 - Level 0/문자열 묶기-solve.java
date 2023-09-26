class Solution {
    public int solution(String[] strArr) {
        int[] answer = new int[31];
        
        for (String str : strArr) {
            answer[str.length()]++;
        }
        
        int max = 0;
        for (int num : answer) {
            if (num > max) max = num; 
        }
        
        return max;
    }
}