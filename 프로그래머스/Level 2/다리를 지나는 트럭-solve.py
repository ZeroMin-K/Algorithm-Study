"""
트럭 여러대가 강을 가로지르는 일차선 다리를 정해진 순으로 건넘
모든 트럭이 다리를 건너려면 최소 몇초 걸리는지
다리에 트럭이 최대 bridge_length대 올라감
weight이하까지 무게 견딤
완전히 오르지 않은 트럭 무게 무시

bridge_length : 다리에 올라갈 수 있는 트럭수 
weight: 다리가 견딜 수 있는 무게 
truck_wieghts: 트럭별 무게 
return : 모든 트럭이 다리를 건너려면 최소 몇초 걸리는지 

다리위나 대기트럭 둘다 앞에서부터 빠짐 => 큐를 이용해서 진행 
"""
# deque import 
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 현재 경과한 시간 total_time 0으로 초기화 
    total_time = 0
    # 현재 다리 건너는 트럭 저장하는 큐 bridge deque로 초기화 
    bridge = deque()
    # truck_weights를 deque로 변경한 waiting_trucks
    waiting_trucks = deque(truck_weights) 
    # 현재 다리위 트럭수 trucks_count 0으로 초기화 
    trucks_count = 0 
    # 현재 다리의 무게 now_weight 0으로 초기화 
    now_weight = 0
    
    # bridge, waitings_trucks가 둘다 빌 때까기 반복 하면서
    while waiting_trucks or bridge: 
        # 1초 경과 total_time 1 증가
        total_time += 1
        
        # bridge가 비어있지 않고 total_time - bridge[0][1]이 bridge_length보다 같거나 크면
        if bridge and total_time - bridge[0][1] >= bridge_length: 
            # truck, time 은 bridge에서 popleft
            truck, time = bridge.popleft() 
            # truck_count 1 감소
            trucks_count -= 1
            # now_weight에 truck만큼 감소
            now_weight -= truck 
        
        # waiting_trucks이 비어있지 않고 \
        # trucks_count가 bridge_length보다 작고 \
        # now_weigth + waiting_trucks[0]이 weight보다 작으면
        if waiting_trucks and \
            trucks_count < bridge_length and \
            now_weight + waiting_trucks[0] <= weight: 
            # truck은 waitings_trucks에서 popleft한 것
            truck = waiting_trucks.popleft() 
            # bridge에 (truck, total_time) 삽입 
            bridge.append((truck, total_time))
            # trucks_count 1증가
            trucks_count += 1
            # now_weight에 truck 만큼 증가 
            now_weight += truck 
            
    # total_time 리턴 
    return total_time