def solution(babblings):
    count = 0
    words = ["aya", "ye", "woo", "ma"]
    for babbling in babblings:
        for word in words:
            if word * 2 not in babbling:
                babbling = babbling.replace(word, ' ')
                
        if len(babbling.strip()) == 0:
            count += 1
    
    return count