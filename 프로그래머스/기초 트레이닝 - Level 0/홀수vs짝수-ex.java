import java.util.stream.IntStream;

class Solution {
    public int solution(int[] num_list) {
        return Integer.max(IntStream.iterate(0, i -> i < num_list.length, i -> i + 2)
                                .map(i -> num_list[i])
                                .sum(), 
                          IntStream.iterate(1, i -> i < num_list.length, i -> i + 2)
                                .map(i -> num_list[i])
                                .sum());
    }
}