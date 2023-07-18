def solution(myString):
    for alpha in myString:
        myString = myString.replace(alpha, 'l') if alpha < 'l' else myString
    return myString