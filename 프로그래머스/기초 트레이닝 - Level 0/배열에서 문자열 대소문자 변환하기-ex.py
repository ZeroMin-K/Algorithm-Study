def solution(strArr):
    return [str.lower() if i % 2 == 0 else str.upper() for i, str in enumerate(strArr)]