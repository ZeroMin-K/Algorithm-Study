class Solution {
    public int solution(String my_string, String target) {
        int length = my_string.length();
        int targetLength = target.length();
        for (int i = 0; i < length; i++) {
            int end = i + targetLength;
            if (end > length) {
                end = length; 
            }
            if (my_string.substring(i, end).equals(target)) {
                return 1;
            }
        }
        return 0;
    }
}