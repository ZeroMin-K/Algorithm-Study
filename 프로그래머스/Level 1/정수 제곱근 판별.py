def solution(n):
    return (n ** (1/2) + 1) ** 2 if (n ** (1/2)).is_integer() else -1