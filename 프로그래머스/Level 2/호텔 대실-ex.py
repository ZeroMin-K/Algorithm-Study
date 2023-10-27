def solution(book_time):
    time_table = [0] * (24 * 60)
    
    for start, end in book_time:
        start_min = 60 * int(start[:2]) + int(start[3:])
        end_min = 60 * int(end[:2]) + int(end[3:]) + 10 
        
        if end_min > 60 * 24 - 1:
            end_min = 60 * 24 - 1
            
        for i in range(start_min, end_min):
            time_table[i] += 1
    
    return max(time_table)