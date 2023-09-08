def solution(myString, pat):
    n = 0
    for i in range(1, len(myString) + 1):
        if myString[:i].endswith(pat):
            n = max(n, i)
    return myString[:n]