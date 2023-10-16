class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        boolean answer = ineq.equals(">") ? n > m : n < m; 
        return (eq.equals("!") ? answer : (answer || n == m)) ? 1 : 0;
    }
}