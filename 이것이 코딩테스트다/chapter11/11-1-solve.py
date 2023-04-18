"""
공포도가 x인 모험가는 반드시 x명 이상 구성한하여 그룹 => 최대 몇개의 그룹을 만들 수 있는지 
공포도 순으로 정렬해서 
해당 공포도만큼 그룹핑해서 개수 세기 

1 2 2 2 3
3 2 2 2 1

1 2 3 4 1 1
=> 1/ 1/ 1/ 2 3 4
=> 4 3 2 1/ 1/ 1

"""

# 모험가 수 n 입력
n = int(input())
# 모험가 공포도 리스트 people 입력
people = list(map(int, input().split()))
# 모험가 공포도 리스트 정렬
people.sort(reverse = True)
# 그룹의 수 total 개수 0으로 초기화 
total = 0 
# 현재 그룹내 사람수 now = 0 
now = 0 
# 정렬된 모험가 공포도 리스트 하나씩 탐색하며  - 원소 person
for person in people: 
    # 현재 공포보다 현재 그룹내 사람수가 작으면
    if person > now: 
        # 사람수 증가하기
        now += 1
    # 아니면
    else: 
        # 그룹 수 증가
        total += 1
        # 현재 그룹내 사람수 0으로 초기화
        now = 0 

# 그룹 수 출력
print(total)