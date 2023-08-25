import java.time.LocalDate;

class Solution {
    public int solution(int[] date1, int[] date2) {
        
        LocalDate days1 = LocalDate.of(date1[0], date1[1], date1[2]);
        LocalDate days2 = LocalDate.of(date2[0], date2[1], date2[2]);
        
        if (days1.isBefore(days2)) return 1;
        return 0;
    }
}