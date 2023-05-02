class Solution {
    public int solution(int[] num_list) {
        int sumTotal = num_list[0];
        int mulTotal = num_list[0];
        int length = num_list.length;
        for (int i = 1; i < length; i++) {
            sumTotal += num_list[i];
            mulTotal *= num_list[i];
        }
                
        return mulTotal > (sumTotal * sumTotal) ? 0: 1;
    }
}