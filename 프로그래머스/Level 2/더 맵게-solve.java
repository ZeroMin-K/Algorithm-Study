import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scovilles, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int mix = 0;
        int first;
        int second; 
        
        for (int scoville : scovilles) pq.add(scoville);
        
        while (pq.size() > 0) {
            first = pq.poll();
            if (first >= k) break;
            
            if (pq.size() == 0) {
                mix = -1;
                break; 
            }
            
            second = pq.poll();
            pq.add(first + second * 2);
            mix++;
        }
        
        return mix;
    }
}