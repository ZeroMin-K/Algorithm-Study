import java.util.*;

class Solution {
    public int solution(int[] num_list) {
        int sum = Arrays.stream(num_list)
            .reduce(Integer::sum)
            .getAsInt();
        int product = Arrays.stream(num_list)
            .reduce((i, j) -> i * j)
            .getAsInt();
        
        return product < sum * sum ? 1 : 0;
    }
}