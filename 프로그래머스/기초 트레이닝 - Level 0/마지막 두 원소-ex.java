class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        int lastIndex = num_list.length - 1;
        int secondIndex = num_list.length - 2;
        
        for (int i = 0; i < num_list.length; i++) {
            answer[i] = num_list[i];
        }
        
        int lastElem = num_list[lastIndex] > num_list[secondIndex] ? 
                    num_list[lastIndex] - num_list[secondIndex] : num_list[lastIndex] * 2;
        answer[answer.length - 1] = lastElem;
        
        return answer;
    }
}