def solution(elements):
    seq_sum_set = set() 
    # 원형 수열 circled_seq는 elements를 이어붙임
    circled_seq = elements + elements 
    
    # 인덱스 length: 원형수열의 길이. 1부터 elements의 길이까지 반복하며
    for length in range(1, len(elements) + 1):
        # 인덱스 i: 원형 수열의 시작점 위치. 0부터 elements의 길이 -1까지 반복하며
        for i in range(len(elements)):
            # 부분 수열 part_seq는 circled_seq를 i부터 i + length까지 슬라이싱함
            part_seq = circled_seq[i: i + length]
            # part_seq의 합을 seq_sums에 삽입
            seq_sum_set.add(sum(part_seq))
    
    return len(seq_sum_set)