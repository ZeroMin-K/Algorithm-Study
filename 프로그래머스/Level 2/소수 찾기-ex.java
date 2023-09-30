import java.util.HashSet;

class Solution {
    public int solution(String numbers) {
        HashSet<Integer> set = new HashSet<>();
        permutations("", numbers, set);
        int count = 0;
        
        while (set.iterator().hasNext()) {
            int num = set.iterator().next();
            set.remove(num);
            if (num == 2) count++;
            if (num % 2 != 0 && isPrime(num)) count++;
        }
        
        return count;
    }
    
    public boolean isPrime(int n) {
        if(n == 0 || n == 1) return false;
        for (int i = 3; i <= (int)Math.sqrt(n); i+= 2) {
            if (n % i == 0) return false; 
        }
        return true; 
    }
    
    public void permutations(String prefix, String str, HashSet<Integer> set) {
        int n = str.length();
        if (!prefix.equals("")) set.add(Integer.valueOf(prefix));
        
        for (int i = 0; i < n; i++) 
            permutations(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n), set);
    }
}