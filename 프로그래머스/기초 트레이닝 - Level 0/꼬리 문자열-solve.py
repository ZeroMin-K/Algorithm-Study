def solution(str_list, ex):
    return ''.join([word for word in str_list if ex not in word])