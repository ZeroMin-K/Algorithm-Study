"""
하나의 키에 여러개의 문자 할당 가능
    - 동일한 키를 연속해서 빠르게 눌러 할당된 순서대로 문자 전환
키의 개수: 1개부터 최대 100개
    특정 키 눌렀을때 입력되는 문자 무작위 배열
    같은 문자가 자판 전체에 여러번 할당 가능
    키 하나에 같은 문자 여러번 할당 가능
    아예 미할당 가능
휴대폰 자판 이용하여 특정 문자열 작성시 키 최소 몇번 눌러야 문자열 작성가능한지 
keymap: 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열 배열
targets: 입력하려는 문자열들이 담긴 문자열 배열 
return : 각 문자열을 작성하기 위해 키를 최소 몇번씩 눌러야하는지 배열
    - 작성불가시 -1 저장 

정확히 어떤걸 몇번 눌러야하는게 아닌 최소 몇번 눌러야하는지만 파악하면되는거라서
keymap을 전부 확인하면서 딕셔너리를 이용하요 각 문자마다 최소 몇번만 누르는지 확인
targets를 하나씩 탐색하면서 해당 문자에 맞게 최소 문자누르는 횟수 확인후 리스트에 저장해서 리턴 
"""


def solution(keymap, targets):
    answer = []
    
    # 각 문자마다 최소 몇번 눌러야하는지 저장하는 key_dict 딕셔너리 생성
    key_dict = dict() 
    # keymap을 하나씩 탐색하면서 - 원소 key
    for key in keymap:
        # key를 enumerate를 이용해서 인덱스 i, 문자 alpha로 열거하여 하나씩 탐색하며
        for i, alpha in enumerate(key):
            # alpha가 key_dict안에 있으면
            if alpha in key_dict:
                # 현재 눌러야하는 횟수 i + 1과 key_dict[alpha] 중 최소값으로 저장
                key_dict[alpha] = min(i + 1, key_dict[alpha])
            # 없으면
            else:
                # key_dict[alpha]는 i + 1 
                key_dict[alpha] = i + 1
                
    # targets를 하나씩 탐색하면서 - 원소 target
    for target in targets: 
        # 현재 문자열을 작성하기 위해 누르는 횟수 pressed 0으로 초기화
        pressed = 0
        # target을 하나씩 탐색하면서 - 원소 alpha
        for alpha in target:
            # alpha가 key_dict안에 있으면
            if alpha in key_dict:
                # pressed에 key_dict[alpha]를 더함
                pressed += key_dict[alpha]
            # 없으면
            else:
                # pressed는 -1로 초기화
                pressed = -1 
                # break
                break
        # pressed를 answer에 삽입
        answer.append(pressed)
    
    return answer