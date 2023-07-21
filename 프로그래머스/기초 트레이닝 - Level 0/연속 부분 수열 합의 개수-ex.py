def solution(elements):
    length = len(elements)
    seq_sum_set = set()
    
    for i in range(length):
        seq_sum = elements[i]
        seq_sum_set.add(seq_sum)
        
        for j in range(i + 1, i + length):
            seq_sum += elements[j % length]
            seq_sum_set.add(seq_sum)
    
    return len(seq_sum_set)