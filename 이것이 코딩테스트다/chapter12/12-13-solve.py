"""
n * n 도시. 1 * 1 크기 칸으로 나뉨. 빈 칸 : 0, 치킨집 : 2, 집 : 1중 하나
(r, c)형태. r행 c열. 1부터 시작 
치킨거리: 집과 가장 가까운 치킨집 사이 거리
    - 집 기준 => 각 집은 치키넉리 가짐
    - 도시의 치킨거리는 모든 집의 치키너길의 합
거리 : |r1 - r2| + |c1 - c2|
도시에 있는 치킨집 중 최대 m개 고르고 나머지 치킨집 모두 폐업.
도시 치킨거리가 가장 작게 될지 구하는 프로그램 

치킨집의 위치 좌표들을 모두 모아서 최대 m개 골라서 그때마다 도시 치킨거리를 구해 가장작은 거리 찾음 
치킨집 m개를 골라서 운영하므로 전체 치킨집 개수에서 m개를 뺀만큼을 운영안하는 방식으로 변경해서 구하기 (0으로 변경)

"""

# 도시 n, 최대 치킨 집 m 입력
n, m = map(int, input().split()) 
# 전체 집 리스트 graph . 빈리스트로 초기화 
graph = [] 
# 치킨집의 좌표를 저장하는 리스트 chickens 빈 리스트로 초기화 
chickens = [] 
# 집의 좌표를 저장하는 리스트 hoses 빈 리스트로 초기화 
houses = [] 

# 인덱스 i: 0부터 n - 1까지 반복하면서 
for i in range(n): 
    # 입력을 받아서 int로 map한 후 리스트로 변환 data
    data = list(map(int, input().split())) 
    # graph에 data 삽입 
    graph.append(data) 
    # 인덱스 j: 0부터 n - 1까지 반복하면서
    for j in range(n):
        # data[j]가 2이면
        if data[j] == 2: 
            # (i, j)를 chickens에 삽입 
            chickens.append((i, j)) 
        # data[j]가 1이면
        elif data[j] == 1: 
            # (i, j)를 houses에 삽입 
            houses.append((i, j)) 

# 도시 최소 치킨 거리 city_min_dist int(1e9)로 초기화 
city_min_dist = int(1e9) 
# combinations import
from itertools import combinations 
# chickens에서 chickens길이 - m만큼 뽑아서 combination으로 만든후 각 케이스를 하나씩 탐색하면서 - 원소 cases
for cases in combinations(chickens, len(chickens) - m): 
    # cases를 하나씩 탐색하면서 - 원소 case
    for case in cases: 
        # graph에서 case[0], case[1] 좌표를 0으로 변경 
        graph[case[0]][case[1]] = 0 

    # 현재 도시 치킨 거리 city_dist 0으로 초기화 
    city_dist = 0 
    # houses를 하나씩 탐색하면서 - 원소 house
    for house in houses: 
        # 현재 집에 치킨거리 chick_dist int(1e9)로 초기화
        chick_dist = int(1e9) 
        # chickens를 하나씩 탐색하면서 - 원소 chicken 
        for chicken in chickens: 
            # graph에서 chicken[0], chicken[1]좌표가 2이면 (치킨집이면) 
            if graph[chicken[0]][chicken[1]] == 2: 
                # 현재 거리 dist 는 house[0] - chicken[0]의 절대값 + house[1] - chicken[1]의 절대값
                dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
                # chick_dist는 dist와 chick_dist중 작은 것으로 저장 
                chick_dist = min(chick_dist, dist) 
        # chick_dist를 city_dist에 더함 
        city_dist += chick_dist 

    # city_min_dist는 city_dist 둘중 작은거로 저장
    city_min_dist = min(city_min_dist, city_dist) 

    # cases를 하나씩 탐색하면서 - 원소 case
    for case in cases: 
        # graph에서 case[0], case[1]좌표를 2로 변경 
        graph[case[0]][case[1]] = 2

# city_min_dist 출력 
print(city_min_dist)