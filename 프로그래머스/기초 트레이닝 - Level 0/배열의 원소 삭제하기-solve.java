import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        int[] answer = {};
        boolean isIn; 
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int num : arr) {
            isIn = false;
            for (int deleteNum : delete_list) {
                if (num == deleteNum) {
                    isIn = true; 
                    break;
                }
            }
            
            if (!isIn) {
                list.add(num);
            }
        }
        
        return list.stream()
                    .mapToInt(i -> i) 
                    .toArray();
    }
}