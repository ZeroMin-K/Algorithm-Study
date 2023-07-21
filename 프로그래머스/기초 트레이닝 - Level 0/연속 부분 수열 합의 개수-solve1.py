"""
원형 수열: 처음과 끝이 연결된 형태의 수열 
elements: 원형 수열의 모든 원소
return : 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수 개수 

인덱스를 두개 붙여서 길이를 1부터 elements길이까지 반복하며
리스트를 슬라이싱하고 sum하여 각 값들을 리스트에 넣은 뒤 set로 변환 후 다시 list로 변경 후 길이를 셈
"""

def solution(elements):
    # 연속 부분수열의 합을 저장하는 리스트 seq_sums 빈 리스트로 초기화 
    seq_sums = [] 
    # 원형 수열 circled_seq는 elements를 이어붙임
    circled_seq = elements + elements 
    
    # 인덱스 length: 원형수열의 길이. 1부터 elements의 길이까지 반복하며
    for length in range(1, len(elements) + 1):
        # 인덱스 i: 원형 수열의 시작점 위치. 0부터 elements의 길이 -1까지 반복하며
        for i in range(len(elements)):
            # 부분 수열 part_seq는 circled_seq를 i부터 i + length까지 슬라이싱함
            part_seq = circled_seq[i: i + length]
            # part_seq의 합을 seq_sums에 삽입
            seq_sums.append(sum(part_seq))
    
    # seq_sums를 set로 변환 후 다시 list로 변환 한뒤 길이 리턴 
    return len(list(set(seq_sums)))