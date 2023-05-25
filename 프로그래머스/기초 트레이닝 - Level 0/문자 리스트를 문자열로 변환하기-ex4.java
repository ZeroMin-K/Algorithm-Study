import java.util.stream.Stream;
import java.util.stream.Collectors;

class Solution {
    public String solution(String[] arr) {
        return Stream.of(arr)
                    .collect(Collectors.joining());
    }
}