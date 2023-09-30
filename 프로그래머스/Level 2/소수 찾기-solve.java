import java.util.HashSet;

class Solution {
    private String[] splitedNumbers; 
    private HashSet<Integer> primes; 
    
    public int solution(String numbers) {
        splitedNumbers = numbers.split("");
        boolean[] visited = new boolean[splitedNumbers.length];
        for (int i = 0; i < visited.length; i++) visited[i] = false; 
        primes = new HashSet<>();
        
        dfs("", visited);
        
        return primes.size();
    }
    
    private void dfs(String result, boolean[] visited) {
        if (result.length() > splitedNumbers.length) return;
        
        if (!result.isEmpty() && checkPrime(Integer.parseInt(result))) 
            primes.add(Integer.parseInt(result));
        
        for (int i = 0; i < splitedNumbers.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(result + splitedNumbers[i], visited);
                visited[i] = false; 
            }
        }
        
    }
    
    private boolean checkPrime(int num) {
        if (num <= 1) return false;
        
        for (int i = 2; i <= (int) Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        
        return true; 
    }
}