"""
중간에 0을 기준으로 인덱스1부터 양쪽으로 하나씩 append하기 
"""

def solution(food):
    answer = ''
    # 앞쪽 부분을 저장할 문자열 header
    header = '' 
    # 인덱스i -  1부터 food길이 마지막까지 탐색하면서 
    for i in range(1, len(food)):
        # 인덱스 i번째 원소를 2로 나누었을 때 몫만큼 반복하면서
        for _ in range(food[i] // 2):
            # header문자열에 인덱스 i 붙이기
            header += str(i)
    # answer에 header 붙이고 0 붙이고 header를 역순으로한 문자열 뭍임 
    answer += header + '0' + header[::-1]
    return answer