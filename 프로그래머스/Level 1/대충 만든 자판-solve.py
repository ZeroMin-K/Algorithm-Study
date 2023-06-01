"""
키의 개수 1개부터 최대 100개 
같은 문자가 자판 전체에 여러번 할당되거나 키 하나에 같은 문자 여러번 할당된 경우, 아예 할당X 경우 있음
휴대폰 자판을 이용해 특정 문자열 작성시 키를 최소한 몇번 눌러야 문자열을 작성 가능한지 
keymap: 1번 키부터 차례대로 할당된 문자들 순서대로 담긴 문자열 배열
    - keymap[i] 는 i+1번 키를 눌렀을때 순서대로 바뀌는 문자열 
    - 행이 몇번 키, 열은 몇번 눌렀는지 
targets: 입력하려는 문자열 담긴 문자열 배열

각 문자열을 작성하기 위해 키를 최소 몇번씩 눌러야하는지 순서대로 배열에 담아 리턴
작성 불가시 -1 저장 

해당 문자를 키맵 문자열 행을 통해서 탐색하면서 가장 최소로 입력하는 것을 찾아서 더해주기 
target 개수 100 * target 원소 최대 길이 100 * keymap 100 * keymap원소길이 100 = 100000000 => 1억 
정확하게 몇번 키를 눌러야하는지는 없고 최소 몇번만 눌러야하는지만 판단하므로
키맵들을 탐색하면서 해당 키에 대한 최소 횟수를 저장하는 딕셔너리를 만들고
target를 하나씩 탐색하면서 키맵 딕셔너리로  최소값을 더해주는 방식으로 진행해보기 
"""

def solution(keymap, targets):
    # 최소 몇번 씩 눌러야하는지 저장하는 리스트 
    answer = []
    
    # 알파벳 키패드 
    keys_dict = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0, \
                'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, \
                'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0, \
                'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0}
    
    # keymap을 하나씩 탐색하면서 : 원소 key 
    for key in keymap: 
        # 인덱스 i : 0부터 key의 길이 -1 까지 반복하면서 
        for i in range(len(key)):
            # key[i]는 현재 문자. i + 1이 key[i]까지 누르는 횟수 
            # keys_dict에 현재 문자 key[i]를 키값으로 했을 때 값이 0이면
            if keys_dict[key[i]] == 0: 
                # keys_dict에서 현재 문자 key[i] 키의 값은 i + 1
                keys_dict[key[i]] = i + 1
            # 그렇지 않으면
            else: 
                # keys_dict에서 현재 문자 key[i] 키의 값은 기존의 값과 i + 1 중 최소값 
                keys_dict[key[i]] = min(keys_dict[key[i]], i + 1) 

    print(keys_dict)
    
    # targets를 하나씩 탐색하면서 : 원소 target
    for target in targets: 
        # 현재 target이 되기 위해 누르는 횟수 press 0으로 초기화
        press = 0
        # target의 문자를 하나씩 탐색하면서 : 원소 i 
        for i in target: 
            # keys_dict에서 target[i]를 키로 press에 값을 더함 
            press += keys_dict[target[i]]
        # 누른 횟수 press를 answer에 append
        answer.append(press) 
        
    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]	
print(solution(keymap, targets))