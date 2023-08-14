def solution(myString):
    return sorted([word for word in myString.split('x') if word])