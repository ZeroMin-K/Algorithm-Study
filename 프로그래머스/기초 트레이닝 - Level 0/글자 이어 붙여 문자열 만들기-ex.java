import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string, int[] index_list) {
        return Arrays.stream(index_list)
                    .mapToObj(operand -> String.valueOf(my_string.charAt(operand)))
                    .collect(Collectors.joining());
    }
}