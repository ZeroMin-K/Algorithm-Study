import java.util.Arrays; 
import java.util.Map;
import java.util.HashMap;

class Solution {
    public String solution(String m, String[] musicinfos) {
        HashMap<String, String> otherSoundsMap = new HashMap<>();
        String[][] otherSounds = new String[][] {{"C#", "H"}, {"D#", "I"}, 
                                                 {"F#", "J"}, {"G#", "K"}, {"A#", "L"}};
        for (String[] otherSound : otherSounds) {
            otherSoundsMap.put(otherSound[0], otherSound[1]);
        }
        
        String targetTitle = "(None)";
        int targetPlayTime = 0;
        int targetIndex = 0; 
        m = convertSheet(otherSoundsMap, m);
 
        for (int i = 0; i < musicinfos.length; i++) {
            String[] musicinfo = musicinfos[i].split(",");
            String sheet = convertSheet(otherSoundsMap, musicinfo[3]);
            int playTime = calPlayTime(musicinfo[0], musicinfo[1]);
            String newSheet = modifySheet(playTime, sheet);
            
            if (newSheet.contains(m)) {
                if ((targetPlayTime < playTime) || 
                    (targetPlayTime == playTime && targetIndex > i)) {
                    targetTitle = musicinfo[2];
                    targetPlayTime = playTime;
                    targetIndex = i; 
                } 
            }
        
        }
        
        return targetTitle;
    }
    
    private int calPlayTime(String startTime, String endTime) {
        String[] start = startTime.split(":");
        String[] end = endTime.split(":");
        
        return Integer.parseInt(end[0]) * 60 + Integer.parseInt(end[1]) 
            - Integer.parseInt(start[0]) * 60 - Integer.parseInt(start[1]);
    }
    
    private String convertSheet(Map<String, String> otherSoundsMap, 
                                String sheet) { 
        for (String key : otherSoundsMap.keySet()) {
            if (sheet.contains(key)) {
                sheet = sheet.replace(key, otherSoundsMap.get(key));
            }
        }
        
        return sheet; 
    }
    
    private String modifySheet(int playTime, String sheet) {
        int length = sheet.length();
        
        if (playTime <= length) {
            return sheet.substring(0, playTime);
        }
        
        return sheet.repeat(playTime / length + 1).substring(0, playTime);
    }
}