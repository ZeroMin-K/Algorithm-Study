import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int n, int k) {
        int numPrime = 0;
        String knumStr = changeKnum(n, k);
        
        for (String knum : knumStr.split("0")) {
            if (knum.length() > 0) {
                if (isPrime(Long.parseLong(knum))) numPrime++;
            }
        }
        
        return numPrime;
    }
    
    private static String changeKnum(int num, int k) {
        List<String> knumStrs = new ArrayList<>();
        StringBuilder knumSb = new StringBuilder();
        
        while (num >= k) {
            knumStrs.add(Integer.toString(num % k));
            num /= k;
        }
        knumStrs.add(Integer.toString(num));
        
        Collections.reverse(knumStrs);
        
        for (String knumStr : knumStrs) {
            knumSb.append(knumStr);
        }
        
        return knumSb.toString();
    }
    
    private static boolean isPrime(long num) {
        if (num == 1) return false;
        
        for (long i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        
        return true;
    }
}