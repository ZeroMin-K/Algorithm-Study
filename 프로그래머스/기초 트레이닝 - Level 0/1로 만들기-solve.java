class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        
        for (int num : num_list) {
            int count = 0;
            while (num != 1) {
                if (num % 2 == 0) num = (int) num / 2;
                else num = (int) (num - 1) / 2;
                count++;
            }
            answer += count; 
        }
        
        return answer;
    }
}