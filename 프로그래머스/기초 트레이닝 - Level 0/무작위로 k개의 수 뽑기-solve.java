import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet; 

class Solution {
    public int[] solution(int[] arr, int k) {
        List<Integer> answer = new ArrayList<>(); 
        Set<Integer> numbers = new HashSet<>();
        
        for (int num : arr) {
            if (numbers.add(num)) answer.add(num); 
            
            if (numbers.size() == k) break; 
        }
        
        while (answer.size() < k) answer.add(-1);
        
        return answer.stream().mapToInt(i -> i).toArray(); 
    }
}