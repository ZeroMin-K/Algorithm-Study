class Solution {
    private static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(0, numbers, 0, target);
        return answer;
    }
    
    private static void dfs(int depth, int[] numbers, int result, int target) {
        if (depth == numbers.length && result == target) {
            answer++;
            return;
        } else if (depth >= numbers.length) {
            return;
        }
        
        dfs(depth + 1, numbers, result + numbers[depth], target);
        dfs(depth + 1, numbers, result - numbers[depth], target);
    }
}