import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> releases = new ArrayList<>();
        Queue<Integer> completesQueue = new LinkedList<>();
        int eachComplete;
        int releaseDay;
        int releaseNum;
        
        for (int i = 0; i < progresses.length; i++) {
            eachComplete = (int) (100 - progresses[i]) / speeds[i];
            if (((100 - progresses[i]) % speeds[i]) != 0) {
                eachComplete++;
            } 
            completesQueue.add(eachComplete);
        }
        
        releaseDay = completesQueue.poll();
        releaseNum = 1;
        while (completesQueue.size() > 0) {
            eachComplete = completesQueue.poll();
            if (eachComplete <= releaseDay) {
                releaseNum++;
            } else{
                releases.add(releaseNum);
                releaseDay = eachComplete;
                releaseNum = 1;
            }
        }
        
        releases.add(releaseNum);
        
        return releases.stream().mapToInt(i -> i).toArray();
    }
}