import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[] priorities, int location) {
        int executionTime;
        int index;
        Queue<Integer[]> queue = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            Integer[] process = new Integer[2];
            process[0] = priorities[i];
            process[1] = i;
            queue.add(process);
        }
        
        for (Integer[] pro: queue) {
            System.out.print(pro[0] + ", " + pro[1] + "  ");
        }
        
        Arrays.sort(priorities);
        
        index = priorities.length - 1;
        executionTime = 1;
        while (!queue.isEmpty()) {
            Integer[] process = queue.poll();
            
            if (process[0] == priorities[index]) {
                if (process[1] == location) {
                    break;
                } else {
                    executionTime++;
                    index--;
                }
            } else {
                queue.add(process);
            }
        }
        return executionTime;
    }
}