def solution(my_string):
    answer = [0] * 52
    for alpha in my_string:
        if alpha.isupper():
            answer[ord(alpha) - ord('A')] += 1
        else:
            answer[(ord('Z') - ord('A') + 1) + ord(alpha) - ord('a')]+= 1
    return answer