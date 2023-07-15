"""
키패드에서 왼손, 오른손 엄지손가락만 이용해서 숫자입력
맨처음 왼속 엄지는 *, 오른속 엄지는 # 위치에서 시작.
엄지사용 규칙
    1. 상, 하, 좌, 우 4가지 방향만 이동. 키패드 이동 한칸은 거리로 1에 해당
    2. 왼쪽 열 3개 숫자 1, 4, 7 입력시 왼손 엄지 사용
    3. 오른쪽 열 3개 숫자 3, 6, 9 입력시 오른손 엄지 사용 
    4. 가운데 열 4개 숫자 2, 5, 8, 0 입력시 두 엄지 손 중 더 가까운 엄지 손가락 사용
        4-1. 두 엄지 손가락 거리 같다면 오른손잡이는 오른손, 왼손잡이는 왼손 사용
numbers: 순서대로 누를 번호 담긴 배열
hand: 왼손잡이 : left, 오른손잡이 : right 
return : 각 번호 누른 엄지 손가락이 왼손인지 오른손인지 나타내는 연속된 문자열 
    L, R

numbers를 하나씩 탐색하면서 해당 숫자에 맞는 키패드 입력해서 문자열에 붙이기 
"""
# 키패드 위치 
keypad_locs = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2), \
               4 : (1, 0), 5 : (1, 1), 6 : (1, 2), \
               7 : (2, 0), 8 : (2, 1), 9 : (2, 2), 0 : (3, 1)}

def cal_dist(start, dest):
    return abs(start[0] - dest[0]) + abs(start[1] - dest[1])
    
def solution(numbers, hand):
    # 각 누른 엄지손가락 문자열 리스트
    uses = [] 
    
    # 왼손 위치 
    left_hand = (3, 0)
    # 오른손 위치 
    right_hand = (3, 2) 
    
    def move_left(number, uses):
        nonlocal left_hand
        left_hand = keypad_locs[number]
        uses.append("L")
    
    def move_right(number, uses):
        nonlocal right_hand 
        right_hand = keypad_locs[number]
        uses.append("R")
    
    # numbers를 하나씩 탐색하면서 - 원소 number 
    for number in numbers: 
        # number가 1, 4, 7 중 하나일 때
        if number in [1, 4, 7]:
            # 왼손 움직임 
            move_left(number, uses) 
        # number가 3, 6, 9 중 하나일 때
        elif number in [3, 6, 9]:
            # 오른손 움직임
            move_right(number, uses) 
        # 나머지의 경우 
        else:
            # 현재 number 위치 number_loc은 number를 키로한 keypad_locs 값 
            number_loc = keypad_locs[number]
            # 왼손에서 number까지 거리
            left_dist = cal_dist(left_hand, number_loc)
            # 오른손에서 number까지 거리
            right_dist = cal_dist(right_hand, number_loc)
            
            # 두 거리가 같으면
            if left_dist == right_dist: 
                
                # 오른손 잡이면
                if hand == 'right':
                    # 오른쪽 사용
                    move_right(number, uses)
                # 나머지(왼손잡이면)
                else:
                    # 왼손 사용
                    move_left(number, uses)
            # 왼손 거리가 작으면
            elif left_dist < right_dist: 
                # 왼손 움직임
                move_left(number, uses)
            # 나머지(오른손 거리가 작으면)
            else: 
                # 오른손 움직임 
                move_right(number, uses)
    
    return ''.join(uses)