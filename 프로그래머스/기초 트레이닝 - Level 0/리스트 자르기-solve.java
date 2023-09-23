import java.util.Arrays;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer;
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        
        answer = Arrays.copyOfRange(num_list, 0, b + 1);
        
        if (n == 2) {
            answer = Arrays.copyOfRange(num_list, a, num_list.length);
        } else if (n == 3) {
            answer = Arrays.copyOfRange(num_list, a, b + 1);
        } else if (n == 4) {
            int length = b - a + 1;
            int newLength = (length % c == 0) ? length / c : (length + 1) / c;
            answer = new int[newLength];
            
            int idx = 0;
            for (int i = a; i <= b; i += c) {
                answer[idx++] = num_list[i];
            }
        }        
        
        return answer;
    }
}