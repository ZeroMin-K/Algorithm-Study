"""
피로도 시스템: 0 이상의 정수. 일정 피로도 사용해 던전 탐험 
최소 필요 피로도: 던전 탐험위해 가지고있어야하는 최소한 피로도
소모 피로도: 던전 탐험 후 소모되는 피로도 
하루에 한번씩 탐험할 수 있는 던전 
던전을 최대한 많이 탐험
k : 현재 피로도 
dungeons: 최소필요 피로도, 소모 피로도가 담긴 2차원 배열
return : 탐험할 수 있는 최대 던전수 
"""

from itertools import permutations

def solution(k, dungeons):
    # 최대 탐험 던전 수 max_completed_dungeons_num 0으로 초기화 
    max_completed_dungeons_num = 0 
    # dugeons를 dungeons길이만큼의 permutations을 하나씩 탐색하며 : 원소 dungeons_order
    for dungeons_order in permutations(dungeons, len(dungeons)):
         # 현재 피로도 now_fatigue k로 초기화 
        now_fatigue = k 
        # 현재 순서로 갔을때 탐험할 수 있는 던전 수 completed_dungeons_num 0으로초기화
        completed_dungeons_num = 0 
        # 던전들의 순서 dungeons_order를 하나씩 탐색하면서 : 원소 dungeon
        for dungeon in dungeons_order: 
            # now_fatigue가 최소 필요 피로도 dungeon[0] 보다 같거나 크면
            if now_fatigue >= dungeon[0]:
                # completed_dungeons_num 1증가
                completed_dungeons_num += 1
                # now_fatigue에 소모 피로도 dungeon[1] 만큼 감소
                now_fatigue -= dungeon[1]
            # 다르면
            else: 
                # 종료 
                break
        # max_completed_dungeons_num과 competed_dungeons_num 중 큰것으로 초기화 
        max_completed_dungeons_num = max(max_completed_dungeons_num, completed_dungeons_num)
    
    # max_completed_dungeons_num 리턴 
    return max_completed_dungeons_num