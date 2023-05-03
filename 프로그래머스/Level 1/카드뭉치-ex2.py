def solution(cards1, cards2, goal):
    
    for _ in range(len(goal)):
        if len(cards1) > 0 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
        elif len(cards2) > 0 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
    
    return "Yes" if len(goal) == 0 else "No"