"""
sequence: 오름차순 정렬된 정수 수열 
k: 부분 수열의 합 
조건 만족하는 부분 수열 찾기
- 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분수열
- 부분 수열의 합은 k
- 합이 k인 부분 수열이 여러개인 경우 길이가 짧은 수열 찾음
- 길이가 짧은 수열이 여러개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열 찾음 

return : 조건을 만족하는 부분수열의 시작 인덱스와 마지막 인덱스를 원소로하는 리스트 
"""

def solution(sequence, k):
    # part_seqs 빈 리스트로 초기화 
    part_seqs = [] 
    # sequence 길이 n
    n = len(sequence) 
    # start, end 0, 0으로 초기화 
    start, end = 0, 0 
    # 현재까지 부분 수열의 합 seq_sum은 sequnce[end]
    seq_sum = sequence[end] 
    
    # start가 n보다 작은 동안 반복 진행 
    while start < n: 
        # seq_sum이 k보다 작고 end가 n보다 작으면 
        if seq_sum < k and end < n: 
            # end 1증가
            end += 1
            # seq_sum에 sequence[end] 값 만큼 증가 
            seq_sum += sequence[end] 
        # 나머지의 경우 
        else: 
            # seq_sum과 k가 같으면
            if seq_sum == k: 
                # part_seqs에 [start, end, end - start + 1] 추가 
                part_seqs.append([start, end, end - start + 1])
            # start 1 증가 
            start += 1
            # seq_sum에 sequence[start] 값 만큼 감소 
            seq_sum -= sequence[start] 

    # part_seqs를 키를 x[2], x[0]로 하여 정렬 
    part_seqs.sort(key = lambda x : (x[2], x[0]))
    # part_seqs[0]에서 첫번째 원소, 두번째 원소를 원소로 한 리스트 반환 
    return [part_seqs[0][0], part_seqs[0][1]]