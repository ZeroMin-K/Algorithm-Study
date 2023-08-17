class Solution {
    public int solution(String number) {
        int answer = 0;
        for (String num : number.split("")) {
            answer += Integer.parseInt(num);
        }
        
        return answer % 9;
    }
}