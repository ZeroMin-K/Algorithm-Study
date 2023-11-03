def solution(a, b, c, d):
    dice_counts = [0] * 7
    for dice in [a, b, c, d]:
        dice_counts[dice] += 1
        
    dice_results = sorted([(dice_count, dice) 
                           for dice, dice_count in enumerate(dice_counts) 
                           if dice_count > 0], 
                          reverse = True)
    
    answer = min(a, b, c, d)
    if dice_results[0][0] == 4: 
        answer = 1111 * dice_results[0][1]
    elif dice_results[0][0] == 3:
        answer = (10 * dice_results[0][1] + dice_results[1][1]) ** 2
    elif dice_results[0][0] == 2:
        p, q = dice_results[0][1], dice_results[1][1]
        answer = (p + q) * abs(p - q) 
        
        if len(dice_results) == 3:
            r = dice_results[2][1]
            answer = q * r
    
    return answer