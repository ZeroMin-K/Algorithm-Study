class Solution {
    public int solution(String[] babblings) {
        int answer = 0;
        String[] words = {"aya", "ye", "woo", "ma"};
        
        for (String babbling : babblings) {
            for (String word : words) {
                if (babbling.contains(word)) 
                    babbling = babbling.replace(word, "0");
            }
            
            babbling = babbling.replace("0", "");
            
            if (babbling.isEmpty()) answer++;
        }
        
        return answer;
    }
}