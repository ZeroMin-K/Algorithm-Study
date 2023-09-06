class Solution {
    public int solution(String skill, String[] skill_trees) {
        int skillLength = skill.length();
        int possibleSkillTreeNum = 0;
        
        for (String skill_tree : skill_trees) {
            int skillIdx = 0;
            int skill_tree_length = skill_tree.length(); 
            boolean isPossibleSkillTree = true;
            
            for (String skillToLearn : skill_tree.split("")) {
                if(skill.contains(skillToLearn)) {
                    if (skillIdx < skillLength && 
                        !skillToLearn.equals(Character.toString(skill.charAt(skillIdx)))) {
                        isPossibleSkillTree = false;
                        break; 
                    } else skillIdx++;
                }
            }
            
            if (isPossibleSkillTree) {
                possibleSkillTreeNum++;
            }
        }
        
        return possibleSkillTreeNum;
    }
}