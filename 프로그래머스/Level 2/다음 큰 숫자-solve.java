class Solution {
    
    public int countOnes(String n) {
        int length = n.length(); 
        int count = 0; 
        for (int i = 0; i < length; i++) {
            if (n.charAt(i) == '1') {
                count++;
            }
        }
        
        return count; 
    }
    
    public int solution(int n) {
        int k = n + 1; 
        int nOnes = countOnes(Integer.toBinaryString(n));
        
        while (true) {
            if (nOnes == countOnes(Integer.toBinaryString(k))) {
                break; 
            } else {
                k++;
            }
        }
        
        return k;
    }
}