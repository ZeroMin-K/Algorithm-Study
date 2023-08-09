class Solution {
    public int calScore(int n, int a, int b, int c) {
        return (int) (Math.pow(a, n) + Math.pow(b, n) + Math.pow(c, n));
    }
    
    
    public int solution(int a, int b, int c) {
        int answer = calScore(1, a, b, c);
        if ((a == b && b != c) || (b == c && a != b) || (c == a && a != b)){
            answer *= calScore(2, a, b, c);
        } else if (a == b && b == c) {
            answer *= calScore(2, a, b, c) * calScore(3, a, b, c);
        } 
        
        return answer;
    }
}