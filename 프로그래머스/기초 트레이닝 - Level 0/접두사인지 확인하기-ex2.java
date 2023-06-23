class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = my_string.indexOf(is_prefix);
        return answer == 0 ? 1 : 0;
    }
}