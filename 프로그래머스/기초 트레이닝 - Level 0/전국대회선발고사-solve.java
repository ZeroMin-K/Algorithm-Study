class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int[] top3 = new int[4]; 
        int targetRank = 1; 
        int candidateRank = 1; 
        
        while (targetRank <= 3) {
            for (int i = 0; i < rank.length; i++) {
                if (rank[i] == candidateRank) {
                    if (attendance[i]) {
                        top3[targetRank] = i;
                        targetRank++;
                    }
                }
            }
            candidateRank++;
        }
        
        return 10000 * top3[1] + 100 * top3[2] + top3[3]; 
    }
}