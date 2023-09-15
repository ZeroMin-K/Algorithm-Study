import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] order) {
        int loadedBoxes = 0;
        int orderIdx = 0;
        
        Stack<Integer> auxBelt = new Stack<>();
        Queue<Integer> belt = new LinkedList<>();
        
        for (int i = 0; i < order.length; i++) {
            auxBelt.add(i + 1);
            while (!auxBelt.isEmpty()) {
                if (auxBelt.peek() == order[orderIdx]) {
                    belt.offer(auxBelt.pop());
                    orderIdx++;
                } else break;
            }
        }
        
        loadedBoxes = belt.size();
        return loadedBoxes;
    }
}