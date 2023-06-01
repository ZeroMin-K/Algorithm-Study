class Solution {
    public int solution(int[] num_list) {
        int answer;
        
        if (num_list.length >= 11) {
            answer = 0;
            for (int num : num_list) {
                answer += num;
            }
        } else {
            answer = 1;
            for (int num : num_list) {
                answer *= num;
            }
        }
        
        return answer;
    }
}