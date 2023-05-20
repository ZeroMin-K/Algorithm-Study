class Solution {
    public int solution(int[] num_list) {
        int mulTotal = num_list[0];
        int sumTotal = num_list[0];
        
        for (int i = 1; i < num_list.length; i++) {
            mulTotal *= num_list[i];
            sumTotal += num_list[i];
        }
        
        return (mulTotal < sumTotal * sumTotal) ? 1: 0;
    }
}