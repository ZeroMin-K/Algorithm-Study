"""
토핑들이 일렬로 올라간 롤케이크 두조각으로 잘라서 동생과 한조각씩 공평하게 나눠먹기
잘린 조각들의 크기, 토핑 개수 상관없이 각 조각에 동일한 가짓수의 토핑이 올라가면 
    공평하게 롤케이크가 나눠진 것으로 생각
topping: 롤케이크에 올려진 토핑들의 번호 저장한 정수 배열
    - 길이 1,000,000 => O(N^2)으로 풀이 불가 
return : 롤케이크를 공평하게 자르는 방법의 수 
    - 공평하게 나눌 수 없으면 0 리턴 
"""

def solution(toppings):
    # 공평하게 나눌 수 있는 방법 수 fair_way 0으로 초기화 
    fair_way = 0 
    # 토핑 종류를 키로, 토핑 개수를 값으로 하는 딕셔너리 toppings_dict 빈 딕셔너리로 생성
    toppings_dict = dict() 
    # toppings를 하나씩 탐색하며 : 원소 topping
    for topping in toppings: 
        # topping이 toppings_dict에 있으면 
        if topping in toppings_dict: 
            # toppings_dict[topping] 1 증가
            toppings_dict[topping] += 1
        # topping이 toppings_dict에 없으면
        else: 
            # toppings_dict[topping]값은 1
            toppings_dict[topping] = 1
    
    # 한쪽 사람의 토핑 종류에 대한 집합 toppings_types 비어있는 집합으로 초기화 
    toppings_types = set() 
    # toppings를 하나씩 탐색하며 : 원소 topping
    for topping in toppings: 
        # toppings_types에 topping 삽입
        toppings_types.add(topping) 
        # toppings_dict[topping] 1 감소
        toppings_dict[topping] -= 1
        # toppings_dict[topping]이 0이면 
        if toppings_dict[topping] == 0: 
            # toppings_dict 에서 topping 삭제 
            del toppings_dict[topping] 
        # toppings_types의 길이와 toppings_dict의 길이가 같으면
        if len(toppings_types) == len(toppings_dict): 
            # fair_way 1 증가 
            fair_way += 1
        
    # fair_way 리턴 
    return fair_way