def solution(myStr):
    answer = [str for str in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if str]
    return answer if answer else ["EMPTY"]