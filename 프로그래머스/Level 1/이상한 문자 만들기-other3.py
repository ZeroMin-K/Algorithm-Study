def solution(s):
    answer = []
    for x in s.split(" "):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        answer.append(word)
    return " ".join(answer)