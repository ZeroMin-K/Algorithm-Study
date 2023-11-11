class Solution {
    public int solution(int storey) {
        int stones = 0;
        while (storey != 0) {
            while (storey % 10 == 0) storey /= 10;
            
             int lastDigit = storey % 10;
        
            if (lastDigit > 5) {
                storey += 10 - lastDigit;
                stones += 10 - lastDigit;
            } else if (lastDigit < 5) {
                storey -= lastDigit;
                stones += lastDigit;
            } else {
                int lastFromSecondDigit = (storey % 100 - lastDigit) / 10;
                if (lastFromSecondDigit >= 5) storey += 5;
                else storey -= 5;
                stones += 5;
            }
        }
        
        return stones;
    }
}