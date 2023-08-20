"""
피로도 시스템 : 0 이상의 정수. 일정 피로도 사용. 던전 탐험
최소 필요 피로도: 해당 던전 탐험위해 가지고있는 최소 피로도
소모 피로도: 던전 탐험후 소모되는 피로도
하루에 한번씩 탐험할 수 있는 여러개의 던전
최대한 많이 탐험 
현재 피로도 k
dungeons: [최소 필요 피로도, 소모피로도] 원소인 2차원 배열
return : 유저가 탐험할 수 있는 최대 던전수 
"""
# permutations import 
from itertools import permutations 

def solution(k, dungeons):
    # 최대 던전수 max_dungeons 0으로 초기화 
    max_dungeons = 0
    # dungeons를 dungeons길이만큼의 permutations를 하나씩 탐색하면서 : 원소 case
    for case in permutations(dungeons, len(dungeons)):
        # 남은 피로도 rest는 k로 초기화
        rest = k
        # 현재 탐험하는 던전수 now_dungeons 0으로 초기화 
        now_dungeons = 0
        # case를 하나씩 탐색하면서 : 원소 dungeon 
        for dungeon in case: 
            # dungeon[0]보다 rest가 크면
            if rest >= dungeon[0]:
                # rest에 dungeon[1] 뺌
                rest -= dungeon[1]
                # now_dungeons 1 증가
                now_dungeons += 1
            # 작으면
            else:
                # break
                break
        # max_dungeons는 now_dungeons와 비교하여 큰것으로 저장 
        max_dungeons = max(max_dungeons, now_dungeons)
    
    # max_dungeons 리턴 
    return max_dungeons