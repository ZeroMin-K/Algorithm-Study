def solution(date1, date2):
    for day1, day2 in zip(date1, date2):
        if day1 < day2:
            return 1
        elif day1 > day2:
            return 0
    return 0