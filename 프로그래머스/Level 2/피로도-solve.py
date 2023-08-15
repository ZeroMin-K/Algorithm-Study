"""
피로도 시스템: 일정 피로도를 사용해서 던전타험
    - 0이상의 정수 
최소 필요 피로도: 해당 던전을 탐험하기 위해 가지고있어야하는 최소한의 피로도 
소모 피로도: 던전 탐험한후 소모되는 피로도 
k: 유저의 현재 피로도 
    - 5000이하
dungeons: 각 던전별 [최소필요 피로도, 소모 피로도]가 담긴 2차원 배열 
    - 던전 개수는 최대 8
return : 유저가 탐험할 수 있는 최대 던전 수 
"""

def solution(k, dungeons):
    # 최대 던전 수 max_dungeon_num 0으로 초기화 
    max_dungeon_num = 0
    
    # permutations import
    from itertools import permutations 
    
    # permutations를 이용하여 dungeons를 dungeons길이 만큼 뽑아 각 경우의 수를 탐색하면서: 원소 case
    for case in permutations(dungeons, len(dungeons)):
        # 현재 경우의수에서 탐험할 수 있는 던전 수 dungeon_num 0으로 초기화
        dungeon_num = 0
        # 남은 피로도 rest_fatigue k로 초기화 
        rest_fatigue = k
        # case의 던전들을 하나씩 탐색하면서 : 원소 dungeon 
        for dungeon in case: 
            # rest_fatigue가 dungeon[0]보다 같거나 크면(최소 필요 피로도보다 남은 피로도가 같거나 더큰경우 - 던전탐험)
            if rest_fatigue >= dungeon[0]:
                # rest_fatigue에서 dungeon[1] 뺌 (남은 피로도에서 현재 던전의 소모피로도 뺌)
                rest_fatigue -= dungeon[1]
                # dungeon_num 1 증가 
                dungeon_num += 1
            # 나머지경우 (최소 필요 피로도보다 낮을때)
            else: 
                # 반복 종료 (탐험종료) 
                break
        # max_dungeon_num은 max_dungeon_num과 dungeon_num중 큰값으로 설정
        max_dungeon_num = max(max_dungeon_num, dungeon_num )
    
    # max_dungeon_num 리턴
    return max_dungeon_num