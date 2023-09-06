def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill)
        
        for skill_to_learn in skill_tree: 
            if skill_to_learn in skill:
                if skill_to_learn != skill_list.pop(0):
                    break
        else:
            answer += 1
            
    return answer