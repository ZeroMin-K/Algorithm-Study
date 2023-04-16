"""
[i, j, k]를 원소로같은 commands를 하나씩 탐색하면서
array를 i부터 j까지 자르고 정렬해서 k번째있는 수를 결과리스트에 넣어서 리턴 

"""

def solution(array, commands):
    # 결과 리스트 
    answer = []
    
    # commands를 하나씩 탐색하면서 - 원소 commands 
    for command in commands:
        # array를 인덱스 commands[0] - 1 부터 commands[1]까지 슬라이싱한 리스트
        # 그 리스트 정렬해서 
        # commands[2]번째 숫자를 answer에 append 
        answer.append(sorted(array[command[0] - 1 : command[1]])[command[2] - 1])
        
    return answer