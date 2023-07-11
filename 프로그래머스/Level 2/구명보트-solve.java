import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int other = 0; 
        
        Arrays.sort(people);
        for (int i = people.length - 1; i >= 0; i--) {
            if (people[i] != 0) {
                if (people[other] != 0 && ((people[i] + people[other]) <= limit)) {
                    people[other] = 0;
                    other++;
                }
                people[i] = 0;
                answer++;
            }
        }
        
        return answer;
    }
}