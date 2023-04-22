"""
n명의 모험가 공포도 측정
공포도가 x인 모험가는 반드시 x명 이상으로 구성
최대 몇개의 모험가 그룹만들 수 있는지

공포도를 오름차순으로 정렬해서 
가자 작은 공포도부터 그룹으로 만들면서 최대 개수 늘리기 
"""

# 모험가 수 n 입력
n = int(input())
# 각 모험가의 공포도 값을 공백으로 구분하여 입력 
people = list(map(int, input().split()))

# 모험가 공포도 리스트 오름차순으로 정렬
people.sort()

# 총 그룹 수 total = 0
total = 0
# 현재 그룹의 인원 now = 0
now = 0
# 모험가 공포도 리스트 하나씩 확인하면서
for person in people:
    # 현재 인원수 now에 현재 인원 추가
    now += 1
    # now가 현재 모험가의 공포도보다 크거나 같으면
    if person <= now:
        # 총 그룹수 total 1증가
        total += 1
        # 현재 그룹수now = 0 초기화
        now = 0
        
# total print 
print(total)