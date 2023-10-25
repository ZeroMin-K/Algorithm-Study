import java.util.Map;
import java.util.HashMap; 

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int targetRank = 1, candidateRank = 1;
        int[] top3 = new int[4];
        
        HashMap<Integer, Integer> students = new HashMap<>();
        for (int i = 0; i < rank.length; i++) students.put(rank[i], i);
        
        while (targetRank <= 3) {
            if (attendance[students.get(candidateRank)]) 
                top3[targetRank++] = students.get(candidateRank);
            candidateRank++;
        }
        
        return top3[1] * 10000 + top3[2] * 100 + top3[3]; 
    }
}