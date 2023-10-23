import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> answer = new ArrayList<>(); 
        
        for (String pixels : picture) {
            StringBuilder newPixels = new StringBuilder();
            for (char pixel : pixels.toCharArray() ) {
                for (int i = 0; i < k; i++) newPixels.append(pixel); 
            }
            
            for (int i = 0; i < k; i++) answer.add(newPixels.toString());
        }
        
        return answer.stream().toArray(String[]::new); 
    }
}