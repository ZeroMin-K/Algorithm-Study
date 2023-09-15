"""
1번 상자부터 n번 상자까지 번호 증가하는 순서로 컨테이너 벨트에 일렬로 놓여 전달
벨트는 한방향으로만 진행 => 벨트 놓인 순서대로 상자내림 
택배 기사가 알려준 순서에 맞게 택배 상자를 실어야함
벨트 앞 상자가 트럭에 실어야하는 순서가 아니면 순서가 될때까지 다른 곳에 보관함
보조 컨테이너 벨트 추가로 설치
    - 한쪽 입구만 있어 맨 앞의 상자만 뺄 수 있음
    - 가장 마지막에 보관한 상자부터 꺼냄
    => 스택 
보조 컨테이너 벨트이용해도 순서대로 상자 못싣으면 상자 싣지않음
order : 기사가 원하는 상자 순서 정수 배열
    - 길이 1,000,000 => O(N^2) 불가 
    - order[i]는 order[i]번째 상자를 i + 1번째로 트럭에 실어야함 
return : 몇개의 상자를 실을 수 있는지 
"""
# deque import 
from collections import deque 

def solution(order):
    # 실을 수 있는 상자수 loaded_boxes_num 0으로 초기화 
    loaded_boxes_num = 0 
    # 1번 상자부터 n번 상자까지 순서의 컨테이너 벨트 boxes_in_belt : order를 정렬한 리스트를 deque로 변환
    boxes_in_belt = deque(sorted(order)) 
    # order를 deque로 변환
    order = deque(order) 
    # 보조 컨테이너 벨트 boxes_in_aux_belt 빈리스트로 초기화 
    boxes_in_aux_belt = [] 
    
    # boxes_in_belt가 빌때까지 반복 
    while boxes_in_belt: 
        # order[0]과 boxes_in_belt[0]이 같으면
        if order[0] == boxes_in_belt[0]: 
            # order popleft
            order.popleft() 
            # boxes_in_belt popleft
            boxes_in_belt.popleft() 
            # loaded_boxes_num 1 증가 
            loaded_boxes_num += 1
        # 다르면
        else: 
            # boxes_in_aux_belt가 비어있지 않고 order[0]과 boxes_in_aux_belt[-1]이 같으면
            if boxes_in_aux_belt and order[0] == boxes_in_aux_belt[-1]:
                # order popleft
                order.popleft() 
                # boxes_in_aux_belt pop
                boxes_in_aux_belt.pop() 
                # loaded_boxes_num 1증가
                loaded_boxes_num += 1
            # 나머지 경우 
            else: 
                # boxes_in_belt를 popleft해서 boxes_in_aux_belt에 삽입 
                boxes_in_aux_belt.append(boxes_in_belt.popleft())
    
    # boxes_in_aux_belt가 빌 때까지 반복
    while boxes_in_aux_belt: 
        # order[0]과 boxes_in_aux_belt[-1]가 같으면
        if order[0] == boxes_in_aux_belt[-1]:
            # order popleft
            order.popleft() 
            # boxes_in_aux_belt pop
            boxes_in_aux_belt.pop() 
            # loaded_boxes_num 1 증가
            loaded_boxes_num += 1
        # 다르면 
        else: 
            # break
            break
            
    # loaded_boxes_num 리턴 
    return loaded_boxes_num