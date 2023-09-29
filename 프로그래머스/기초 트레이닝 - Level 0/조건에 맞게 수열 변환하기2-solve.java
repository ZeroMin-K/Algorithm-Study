class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        for (int num : arr) {
            int result = num;
            int rep = 0;
            while (check(result)) {
                if (result >= 50 && result % 2 == 0) result /= 2;
                else if (result < 50 && result % 2 == 1) result = result * 2 + 1;
                
                rep++;
            }
            
            answer = Math.max(answer, rep);
        }
        
        return answer;
    }
    
    private boolean check(int result) {
        if ((result > 50 && result % 2  == 1) ||
           (result < 50 && result % 2 == 0)) return false;
        return true;
    }
}