class Solution {
    public String[] solution(String[] strArr) {
        int length = strArr.length;
        String[] answer = new String[length];
        
        for (int i = 0; i < length; i++) {
            if (i % 2 == 0) {
                answer[i] = strArr[i].toLowerCase();
            } else {
                answer[i] = strArr[i].toUpperCase();
            }
        }
        
        return answer;
    }
}