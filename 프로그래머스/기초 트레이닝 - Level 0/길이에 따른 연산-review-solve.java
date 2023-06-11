class Solution {
    public int solution(int[] num_list) {
        int answer;
        if (num_list.length >= 11) {
            answer = 0;
            for (int num : num_list) {
                answer += num;
            }
        } else {
            answer = num_list[0];
            for (int i = 1; i < num_list.length; i++) {
                answer *= num_list[i];
            }
        }
        
        return answer;
    }
}