def solution(my_strings, parts):
    return ''.join(string[part[0] : part[1] + 1] for string, part in zip(my_strings, parts))