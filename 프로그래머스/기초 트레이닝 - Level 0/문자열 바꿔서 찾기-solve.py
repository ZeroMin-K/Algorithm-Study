def solution(myString, pat):
    myString = myString.replace('A', 'b')
    myString = myString.replace('B', 'A')
    myString = myString.replace('b', 'B')
    return 1 if pat in myString else 0