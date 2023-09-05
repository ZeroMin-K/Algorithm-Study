import java.util.Stack;

class Solution {
    public int[] solution(int[] prices) {
        int[] periods = new int[prices.length];
        Stack<int[]> records = new Stack<>();
        
        for (int i = 0; i < prices.length; i++) {
            while(!records.isEmpty() && prices[i] < records.peek()[1]) {
                int[] record = records.pop();
                periods[record[0] - 1] = (i + 1) - record[0];
                
            }
            
            records.push(new int[] {i + 1, prices[i]});
        }
        
        while (!records.isEmpty()) {
            int[] record = records.pop();
            periods[record[0] - 1] = prices.length - record[0];
        }
        
        return periods;
    }
}