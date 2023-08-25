class Solution {
    public int solution(int[] date1, int[] date2) {
        int[] days = {365, 30, 1};
        int total1 = 0;
        int total2 = 0;
        for (int i = 0; i < 3; i++) {
            total1 += days[i] * date1[i];
            total2 += days[i] * date2[i];
        }
        
        return total1 < total2 ? 1 : 0;
    }
}