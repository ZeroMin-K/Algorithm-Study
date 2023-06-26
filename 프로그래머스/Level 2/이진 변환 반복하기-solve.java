class Solution {
    public int[] solution(String s) {
        
        // 0번 인덱스: 변환횟수, 1번 인덱스: 제거된 0의 개수 
        int[] answer = new int[2];
        
        // 1의 개수 저장하는 oneCounts 0으로 초기화 
        int oneCounts = 0;
        
        // 문자열 s가 "1"이 아닌 동안 반복하면서 
        while (!s.equals("1")) {
            // 문자열 s에서 1의 개수 oneCounts를 셈
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '1') {
                    oneCounts++;
                }
            }
            // 문자열 s의 길이에서 1의 개수를 빼 answer[1]에 더함 
            answer[1] += s.length() - oneCounts; 
            // oneCounts를 2진수로 변환하여 문자열 s에 대입 
            s = Integer.toBinaryString(oneCounts);
            
            // 변환횟수 answer[0] 1증가. 
            answer[0]++;
            // 1의 개수 oneCounts0으로 초기화 
            oneCounts = 0;
            
        }
        
        return answer;
        
    }
}