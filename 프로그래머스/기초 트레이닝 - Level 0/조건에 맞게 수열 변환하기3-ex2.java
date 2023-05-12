import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int k) {
        return Arrays.stream(arr)
                    .map(op -> k % 2 == 0 ? op + k : op * k)
                    .toArray();
    }
}