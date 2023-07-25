def solution(citations):
    h_index = 0
    citations.sort()
    
    for i in range(len(citations)):
        if citations[i] >= len(citations) - i:
            h_index += 1
            
    return h_index