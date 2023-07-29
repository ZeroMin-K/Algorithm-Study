class Solution {
    public int solution(String myString, String pat) {
        return myString.replace("A", "b")
                    .replace("B", "A")
                    .replace("b", "B")
                    .contains(pat) ? 1 : 0;
    }
}