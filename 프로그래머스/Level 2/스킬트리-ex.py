def solution(skill, skill_trees):
    possible_skill_tree_num = 0
    
    for skill_tree in skill_trees:
        skill_order = [s for s in skill_tree if s in skill]
        if skill_order == list(skill)[:len(skill_order)]:
            possible_skill_tree_num += 1
            
    return possible_skill_tree_num