import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        List<Integer> colSeq = new ArrayList<>();
        int lastNum;
        colSeq.add(n);
        
        lastNum = colSeq.get(colSeq.size() - 1);
        while (lastNum != 1) {
            int nextNum = 3 * lastNum + 1;
            if (lastNum % 2 == 0) {
                nextNum = lastNum / 2;
            }
            colSeq.add(nextNum);
            lastNum = colSeq.get(colSeq.size() - 1);
        }
        
        return colSeq.stream()
                    .mapToInt(i -> i)
                    .toArray();
    }
}