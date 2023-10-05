class Solution {
    public int[] solution(String my_string) {
        int arrLength = (int) 'Z' - (int) 'A' + (int) 'z' - (int) 'a' + 2;
        int[] answer = new int[arrLength];
        int length = my_string.length();
        
        for (int i = 0; i < length; i++) {
            char c = my_string.charAt(i);
            if (c >= 'a') 
                answer[c - 'a' + 'Z' - 'A' + 1]++;
            else 
                answer[c - 'A']++;
        }
        
        return answer;
    }
}