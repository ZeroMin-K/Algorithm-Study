import java.util.HashSet; 

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        HashSet<String> hashSet = new HashSet<>();
        hashSet.add(words[0]);
        
        for (int i = 1; i < words.length; i++) {
            if (words[i-1].charAt(words[i - 1].length() - 1) != words[i].charAt(0) ||
               hashSet.contains(words[i])) {
                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1; 
                break; 
            }
            hashSet.add(words[i]);
        }

        return answer;
    }
}