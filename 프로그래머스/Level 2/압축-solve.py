"""
LZW 압축 과정
1. 길이가 1인 모든 단어를 포함하도록 사전 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾음 
3. w에 해당하는 사전의 색인 번호를 출력, 입력에서 w제거
4. 입력에서 처리되지 않은 다음 글자가 남아있다면 (c), w + c에 해당하는 단어를 사전에 등록
5. 단계로 2로 돌아감
영문 대문자만 처리. 사전의 색인번호는 정수값. 1부터 시작
msg: 영문 대문자로만 이뤄진 문자열 
    - 1글자 이상 1000 글자 이하
return : msg를 압축한 후 사전 색인 번호를 배열로 출력 
"""

def solution(msg):
    # 압축한 문자열의 색인번호를 저장하는 리스트 compressed_indices : 빈리스트로 초기화 
    compressed_indices = [] 
    # 문자열을 키, 색인번호를 값으로 갖는 사전 index_dict 생성
    # 키는 A부터 Z까지 값은 1부터 26까지로 생성 
    index_dict = {chr(i) : i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    # 마지막 인덱스 last_index 27으로 초기화 
    last_index = 27 
    
    # 현재 입력 시작 인덱스 start 0으로 초기화
    start = 0 
    # 인덱스 i : 0부터 msg의 길이 - 1까지 반복하면서
    for i in range(len(msg)):
        # 현재 i가 시작인덱스가 아니면 넘어감 
        if i != start:
            continue 
        # 인덱스 j: msg의 길이부터 i + 1까지 반복하면서 
        for j in range(len(msg), i, -1):
            # 현재 단어 w는 msg를 i부터 j까지 슬라이싱한 문자열 
            w = msg[i: j]
            # w가 index_dict에 있으면
            if w in index_dict: 
                # compressed_indices에 index_dict[w] 삽입 
                compressed_indices.append(index_dict[w])
                # j가 len(msg) - 1보다 작으면 
                if j < len(msg) - 1:
                    # index_dict[w + msg[j + 1]]은 last index 값으로 설정
                    index_dict[w + msg[j]] = last_index
                    # last index 1 증가 
                    last_index += 1
                # 시작 인덱스를 j부터로 초기화
                start = j
                # 현재 반복 종료 
                break 
    
    # compressed_indices 리턴 
    return compressed_indices