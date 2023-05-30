"""
키패드에서 왼손, 오른손 엄지 손가락만 이용해서 숫자만 입력
맨처음 왼손 엄지손가락은 * 키패드, 오른손 엄지손가락은 # 키패드 위치에서 시작
엄지손가락 사용 규칙
1. 엄지손가락은 상, 하, 좌, 우 4가지 방향으로만 이동. 키패드 이동한칸은 거리로 1 
2. 왼쪽 열 3개숫자 1, 4, 7 입력시 왼손 엄지 손가락 사용
3. 오른쪽 열 3개숫자 3, 6, 9 입력시 오른손 엄지 손가락 사용
4. 가운데 열 4개숫자 2, 5, 8, 0 입력시 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지 손가락 사용
    4-1. 두 엄지 손가락 거리 같다면 오른손잡이는 오른손 엄지, 왼손잡이는 왼손 엄지손가락 사용
    
numbers: 순서대로 누를 번호 담긴 리스트
hand: 왼손잡이, 오른손잡이 여부 문자열 left, right
return : 각 번호를 누른 엄지손가락이 왼손인지, 오른손인지 연속된 문자열 형태로 리턴 
    - 왼손 엄지 사용시 L, 오른손 엄지 사용시 R 순서대로 이어붙여 문자열 형태 

numbers를 하나씩 탐색하면서, 어떤 엄지 손일지 문자열에 이어붙이기 

1 2 3   L,(0, 0) X,(0, 1) (0, 2)
4 5 6   L,(1, 0) X,(1, 1)
7 8 9   L,(2, 0) X,(2, 1)
* 0 #   L,(3, 0) (3, 1) (3, 2)
키패드는 4 * 3 크기의 2차원 리스트 
1 : (0, 0), ... # : (3, 2) 
""" 

def solution(numbers, hand):
    # 결과 문자열 
    answer = ''
    
    # 키패드에 따른 좌표 1, 2, 3, 4, 5, 6, 7, 8, 9, *, 0, #
    pads = {1 : (0,0), 2: (0, 1), 3 : (0, 2), \
            4 : (1, 0), 5 : (1, 1), 6 : (1, 2), \
            7 : (2, 0), 8 : (2, 1), 9 : (2, 2), \
            '*' : (3, 0), 0 : (3, 1), '#' : (3, 2)} 
    # 왼손잡이, 오른손잡이 여부 
    main = {"left" : 'L', "right" : "R"}
    
    # 왼손 엄지의 위치 처음에 *
    left_thumb = pads['*']
    # 왼손 엄지로 누를 수 있는 리스트 (1, 4, 7)
    left_side = [1, 4, 7]
    # 오른손 엄지의 위치 처음에 # 
    right_thumb = pads['#']
    # 오른손 엄지로 누를 수 있는 리스트 (3,6,9) 
    right_side = [3, 6, 9]
    
    def cal_dist(thumb, number):
        nonlocal pads 

        dist_x = pads[number][0] - thumb[0]
        dist_y = (pads[number][1] - thumb[1])

        return abs(dist_x) + abs(dist_y)

    def move_left(answer, number):
        nonlocal left_thumb
        nonlocal pads 

        answer += "L"
        left_thumb = pads[number]
        return answer 

    def move_right(answer, number):
        nonlocal right_thumb
        nonlocal pads 

        answer += "R"
        right_thumb = pads[number]
        return answer
        
    # numbers를 하나씩 탐색하면서 - 원소 number
    for number in numbers:     
        # 현재 번호가 왼손 엄지로 누를 수 있는 리스트에 있으면
        if number in left_side: 
            answer = move_left(answer, number)
        # 혹은 현재 번호가 오른손 엄지로 누를 수 있는 리스트에 있으면
        elif number in right_side:
            answer = move_right(answer, number)
        # 나머지 (2, 5, 8, 0 이면)
        else:
            # 왼손 엄지로부터 2,5, 8, 0까지의 거리
            left_dist = cal_dist(left_thumb, number)
            # 오른손 엄지로부터 2, 5, 8, 0까지의 거리
            right_dist = cal_dist(right_thumb, number)
            
            # 둘이 서로 거리가 같으면
            if left_dist == right_dist:
                if hand == 'left':
                    answer = move_left(answer, number)
                else:
                    answer = move_right(answer, number)
            # 왼손 엄지가 더 멀면 오른손 엄지가 움직임 
            elif left_dist > right_dist:
                answer = move_right(answer, number)
            # 나머지 (오른손 엄지가 더 멀면) 왼손 엄지가 움직임 
            else:
                answer = move_left(answer, number)
    return answer