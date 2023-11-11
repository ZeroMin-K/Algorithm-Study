class Solution {
    public int solution(String[] babblings) {
        int answer = 0;
        String[] words = {"aya", "ye", "woo", "ma"};
        
        for (String babbling : babblings) {
            for (String word : words) {
                if (babbling.contains(word)) 
                    babbling = babbling.replace(word, "0");
            }
            
            boolean canSpeak = true; 
            for (char ba : babbling.toCharArray()) {
                if (ba != '0') {
                    canSpeak = false;
                    break; 
                }
            }
            
            if (canSpeak) answer++;
        }
        
        return answer;
    }
}