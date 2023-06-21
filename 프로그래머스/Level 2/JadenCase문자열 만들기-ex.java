class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.toLowerCase().split("");
        boolean flag = true;
        
        for (String str: strArr) {
            answer += flag ? str.toUpperCase() : str;
            flag = str.equals(" ") ? true : false; 
        }
        
        return answer;
    }
}