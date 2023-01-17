def solution(x):
    num = list(map(int, str(x)))
    return True if x % sum(num) == 0 else False