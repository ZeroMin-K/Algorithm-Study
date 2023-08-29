"""
n * n 도시. 1 * 1 크기 칸으로 나누어짐
각 칸은 빈칸, 치킨집, 집 중 하나
0 : 빈칸, 1 : 집, 2 : 치킨 집 
도시 칸 (r, c) 형태 : r행 c열. 위에서부터 r번째칸, 왼쪽에서부터 c번째칸. 1부터 시작
치킨 거리 : 집과 가장 가까운 치킨집 사이 거리
    - 치킨 거리는 집 기준
    - 각각의 집은 치킨거리 가짐
    - 도시의 치킨거리는 모든 집의 치킨 거리함
(r1, c1), (r2, c2)의 거리: |r1 - r2| + |c1 - c2|
가장 수익을 많이 낼수 있는 치킨집의 개수 최대 M개
치킨집 중에서 최대 M개를 고르고 나머지 치킨집 폐업.
어떻게 골라야 도시의 치킨거리가 가장 작게될지 
print: 폐업시키지 않을 치킨집 최대 M개 골랐을때 도시의 치킨 거리 최솟값 출력 

도시의 치킨거리가 가장 작아지려면 결국 치킨집이 많아야 각 집마다 치킨거리 짧아짐
무조건 m개를 골라야 이득
각 치킨집들을 m개만큼 고르면서
    각 집들마다 치킨집과 거리확인하면서 치킨거리 찾아
    총 도시 치킨거리 계산
총 도시 치킨거리중에서 가장 작은 치킨거리 찾기 
"""

# n, m 입력
n, m = map(int, input().split())

# 치킨집들의 좌표를 저장하는 리스트 chickens : 빈리스트로 초기화 
chickens = [] 
# 집의 좌표를 저장하는 리스트 houses: 빈 리스트로 초기화 
houses = [] 

# 인덱스 i: 0부터 n - 1까지 반복하면서 
for i in range(n):
    # 도시 정보를 공백구분으로 int로 변환뒤 list로 변경 data
    data = list(map(int, input().split()))
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(n):
        # data[j]가 1이면 (집)
        if data[j] == 1:
            # houses에 (i, j) 삽입 
            houses.append((i, j)) 
        # data[j]가 2이면 (치킨집)
        elif data[j] == 2: 
            # chickens에 (i, j) 삽입 
            chickens.append((i, j)) 
            
# 최소 도시 치킨 거리 min_city_dist 1e9로 초기화
min_city_dist = int(1e9) 
# combinations import 
from itertools import combinations 
# chickens를 m번 뽑는 combination을 반복하면서 : 원소 combi_case
for combi_case in combinations(chickens, m): 
    # 현재 도시 치킨 거리 city_dist : 0으로 초기화
    city_dist = 0 
    # houses를 하나씩 탐색하면서: 원소 house
    for house in houses: 
        # 현재 집의 치킨 거리 house_dist 1e9로 초기화
        house_dist = int(1e9) 
        # combi_case를 하나씩 탐색하면서: 원소 chicken
        for chicken in combi_case: 
            # 치킨집마다 계산한 치킨거리 dist |house[0] - chicken[0]| + |house[1] - chicken[1]|
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            # house_dist와 dist중 작은것으로 hose_dist에 저장
            house_dist = min(dist, house_dist)
        # house_dist를 city_dist에 더함 
        city_dist += house_dist
    # city_dist와 min_city_dist중 작은값으로 min_city_dist 변경 
    min_city_dist = min(city_dist, min_city_dist)
    
# min_city_dist 출력 
print(min_city_dist)