def solution(str1, str2):
    return ''.join([alpha1 + alpha2 for alpha1, alpha2 in zip(str1, str2)])