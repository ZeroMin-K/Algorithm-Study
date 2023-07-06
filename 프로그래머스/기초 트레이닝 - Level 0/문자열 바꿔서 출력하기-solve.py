def solution(myString, pat):
    changed_string = ""
    for alpha in myString:
        if alpha == "A":
            changed_string += "B"
        elif alpha == "B":
            changed_string += "A"
        else:
            changed_string += alpha 
            
    return 1 if pat in changed_string else 0