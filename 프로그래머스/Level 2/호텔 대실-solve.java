import java.util.Arrays;

class Solution {
    public int solution(String[][] book_time) {
        int timesLength = 24 * 60;
        int[] times = new int[timesLength];
        
        for (String[] time : book_time) {
            int startTime = convertTime(time[0]);
            int endTime = convertTime(time[1]);
            endTime = (endTime + 9) >= timesLength ? timesLength : endTime + 10; 
            
            for (int i = startTime; i < endTime; i++) times[i]++;
        }
        
        return Arrays.stream(times).max().getAsInt();
    }
    
    private int convertTime(String time) {
        String[] hourAndMin = time.split(":");
        return Integer.parseInt(hourAndMin[0]) * 60 + Integer.parseInt(hourAndMin[1]); 
    }
}