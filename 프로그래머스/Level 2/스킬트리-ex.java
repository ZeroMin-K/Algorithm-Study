class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = -1;
        int possibleSkillTreeNum = 0;
        
        for (String skill_tree : skill_trees) {
            if (isPossibleSkillTree(skill, skill_tree)) {
                possibleSkillTreeNum++;
            }
        }
        
        return possibleSkillTreeNum; 
    }
    
    private boolean isPossibleSkillTree(String skill, String skill_tree) {
        int skillIdx = 0;
        
        for (char skillToLearn : skill_tree.toCharArray()) {
            if (skill.indexOf(skillToLearn) != -1) {
                if (skill.charAt(skillIdx) != skillToLearn) {
                    return false; 
                }
                skillIdx++;
            }
        }
        
        return true; 
    }
}