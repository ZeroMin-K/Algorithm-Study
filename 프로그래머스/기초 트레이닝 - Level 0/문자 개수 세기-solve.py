def solution(my_string):
    return [ my_string.count(chr(alpha)) 
                for start, end in [[ord('A'), ord('Z') + 1], [ord('a'), ord('z') + 1]]
                    for alpha in range(start, end)]