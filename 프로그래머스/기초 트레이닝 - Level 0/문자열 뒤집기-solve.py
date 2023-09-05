def solution(my_string, s, e):
    return my_string[:s] + my_string[e:s - 1:-1] + my_string[e + 1:] \
            if s != 0 else my_string[e::-1] + my_string[e + 1:]