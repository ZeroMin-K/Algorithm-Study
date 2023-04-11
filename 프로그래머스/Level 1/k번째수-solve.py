"""
배열array i번째 숫자부터 j번재 숫자까지 자르고 정렬했을 때 k번째 수 구하기 
commands를 하나씩 탐색하면서 array를 슬라이싱하며 k번째 수를 찾아 정답 리스트에 append해서 결과 반환하기
"""

def solution(array, commands):
    answer = []
    # commands를 하나씩 탐색 - command
    for command in commands:
        # command -  i번째 숫자부터 command[0], j번째 숫자까지 자르고 command[1], k번째 수 command[2]
        # array를 command[0]부터 command[1] + 1까지 슬라이스한 리스트에서 command[2]번째 수를 찾아서 answer에 append
        # j가 array 길이보다 같거나 작으면 마지막 길이를 j까지 
        end = command[1]
        # # j가 array 길이보다 크면 
        if command[1] >= len(array):
            # 마지막 길이를 array길이까지
            end = len(array)
            
        # 새로운 리스트 생성
        new_array = array[command[0] - 1 : end]
        new_array.sort()
        
        answer.append(new_array[command[2] -1])

        
    return answer