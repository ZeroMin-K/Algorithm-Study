class Solution {
    public int solution(int a, int b) {
        int ab = Integer.valueOf(Integer.toString(a) + Integer.toString(b));
        int ba = Integer.valueOf(Integer.toString(b) + Integer.toString(a));
        return ab >= ba ? ab : ba;
    }
}