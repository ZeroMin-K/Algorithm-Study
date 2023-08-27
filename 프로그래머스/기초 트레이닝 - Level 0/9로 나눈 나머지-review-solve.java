class Solution {
    public int solution(String number) {
        int answer = 0;
        for (String num : number.split("")) {
            if (num.length() > 0) {
                answer += Integer.parseInt(num);
            }
        }
        
        return answer % 9;
    }
}