def solution(n, control):
    controls = {"w" : 1, "s" : -1, "d" : 10, "a" : -10}
    return n + sum([controls[move] for move in control])