def solution(myStr):
    for sep in ['a', 'b', 'c']:
        myStr = myStr.replace(sep, ' ')
    answer = [str for str in myStr.split() if str]
    return answer if answer else ["EMPTY"]