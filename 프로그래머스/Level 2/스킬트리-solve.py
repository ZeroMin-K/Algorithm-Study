"""
skill: 선행 스킬 순서
    - 알파벳 대문자. 문자열 표기 
    - 중복 x. 길이 26이하 
skill_tress: 스킬트리 
    - 문자열 표기 
    - 길이 20이하 
    - 원소는 길이 26이하 중복x
return : 가능한 스킬 트리 개수 
"""
def solution(skill, skill_trees):
    answer = -1
    # skill_len skill의 길이로 초기화
    skill_len = len(skill)

    # 가능한 스킬 트리 개수 possibe_skill_tree_num 0으로 초기화 
    possible_skill_tree_num = 0 
    # skill_trees를 하나씩 탐색하면서 : 원소 skill_tree 
    for skill_tree in skill_trees: 
        # 선행 스킬의 인덱스 skill_idx 0으로 초기화 
        skill_idx = 0 
        # 현재 스킬트리가 가능한지 여부 is_possible_skill_tree True로 초기화 
        is_possible_skill_tree = True 
        # skill_tree를 하나씩 탐색하면서 : 원소 skill_to_learn
        for skill_to_learn in skill_tree: 
            # skill_to_learn이 skill에 있으면
            if skill_to_learn in skill: 
                # skill_idx가 skill_len보다 작고 skill[skill_idx]와 skill_to_learn이 다르면
                if skill_idx < skill_len and skill[skill_idx] != skill_to_learn: 
                    # is_possible_skill_tree False로 변경 (현재 스킬트리 불가)
                    is_possible_skill_tree = False 
                    # break
                    break 
                # 같으면 
                else: 
                    # skill_idx 1 증가 
                    skill_idx += 1
                    
        # is_possible_skill_tree 가 True이면 (현재 스킬트리가 가능하다면)
        if is_possible_skill_tree: 
            # possible_skill_tree_num 1증가 
            possible_skill_tree_num += 1
    
    # possible_skill_tree_num 리턴 
    return possible_skill_tree_num