def solution(date1, date2):
    total1 = 0 
    total2 = 0
    for day1, day2, days in zip(date1, date2, [365, 30, 1]):
        total1 += days * day1
        total2 += days * day2
        
    return int(total1 < total2)