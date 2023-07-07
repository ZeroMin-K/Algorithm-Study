class Solution
{
    public int solution(int n, int a, int b)
    {
        int round = 1;
        int aGroup;
        int bGroup;
        
        if (a > b) { 
            int temp = a;
            a = b;
            b = temp; 
        }
        
        while (a >= 1) {
            aGroup = (a % 2 == 0) ? a / 2 : (a + 1) / 2;
            bGroup = (b % 2 == 0) ? b / 2 : (b + 1) / 2;
            
            if (aGroup == bGroup) {
                break;
            }
            
            a = aGroup;
            b = bGroup;
            round++;
        }
        
        return round;
    }
}