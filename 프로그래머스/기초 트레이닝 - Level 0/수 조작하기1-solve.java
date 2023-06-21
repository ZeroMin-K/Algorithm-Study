import java.util.*;

class Solution {
    public int solution(int n, String control) {
        int answer = n;
        int length = control.length();
        HashMap<Character, Integer> hashMap = new HashMap<>();
        hashMap.put('w', 1);
        hashMap.put('s', -1);
        hashMap.put('d', 10);
        hashMap.put('a', -10);
        
        for (int i = 0; i < length; i++) {
            answer += hashMap.get(control.charAt(i));
        }
        
        return answer;
    }
}