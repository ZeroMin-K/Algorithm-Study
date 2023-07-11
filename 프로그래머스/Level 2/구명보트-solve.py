"""
구명보트: 한번에 최대 2명씩, 무게 제한 
people: 사람 몸무게 담은 배열 
limit: 구명보트 무게 제한 
return : 모든 사람 구출하기 위해 필요한 구명보트 개수 최솟값 

사람 몸무게 정렬 후 제일 무거운 사람부터 보트에 태우면서 그다음으로 무거운 사람으로 무게 제한에 맞게 채우기 
"""

def solution(people, limit):
    # 구명 보트 개수 boat_num 0으로 초기화
    boat_num = 0
    
    # people 역순 정렬
    people.sort(reverse = True) 
    
    # 가장 가벼운 사람의 인덱스 last . people 길이 - 1로 초기화 
    last = len(people) - 1
    
    # 인덱스 i: 0부터 people길이만큼 반복하면서
    for i in range(len(people)):
        # people[i]가 0이 아니면 (보트에 태우지 않은 사람이면) 
        if people[i] != 0:
            # people[last]가 0이 아니고 people[i] + people[last]가 limit보다 작거나 같으면
            if people[last] != 0 and (people[i] + people[last]) <= limit:
                    # people[last] 0으로 초기화 (같이 보트에 태움)
                    people[last] = 0
                    # last 1 감소
                    last -= 1
            # boat_num 1증가
            boat_num += 1
            # people[i] 0으로 변경
            people[i] = 0
    
    return boat_num