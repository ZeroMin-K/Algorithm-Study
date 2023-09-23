import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<int[]> bridge = new LinkedList<>();
        int waitingIndex = 0;
        int totalTime = 0;
        int trucksCount = 0;
        int nowWeight = 0;
        
        while (waitingIndex < truck_weights.length || !bridge.isEmpty()) {
            totalTime++;
            
            if (!bridge.isEmpty() && totalTime - bridge.peek()[1] >= bridge_length) {
                int[] truck = bridge.poll();
                trucksCount--;
                nowWeight-= truck[0];
                
            }
            
            if (waitingIndex < truck_weights.length && 
               trucksCount < bridge_length &&
               nowWeight + truck_weights[waitingIndex] <= weight) {
                int truck = truck_weights[waitingIndex];
                bridge.offer(new int[] {truck_weights[waitingIndex], totalTime});
                trucksCount++;
                nowWeight += truck;
                waitingIndex++;
            }
        }
        
        return totalTime;
    }
}