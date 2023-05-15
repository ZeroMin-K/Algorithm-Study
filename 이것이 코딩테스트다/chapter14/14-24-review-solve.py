"""
특정 위치 집에 한개 안테나 설치 - 안테나로부터 모든 집까지 거리의 총합이 최소

안테나를 각 위치중 가장 중앙에 놓으면 최소값이 됨
리스트 0 1 2 3 중앙 인덱스 1 (길이4)
리스트 0 1 2 3 4 중앙 인덱스 2 (길이5)

(4-1) // 2 => 1 
(4//2) - 1 => 1
(5-1) // 2 => 2
(5//2) - 1 => 1
"""

# 집의 수 n 입력
n = int(input())
# 공백 기준으로 n채의 집 위치 리스트 입력
houses = list(map(int, input().split()))

# 집 위치 리스트 정렬
houses.sort()

# 집 위치리스트의 중앙값 출력 
print(houses[(len(houses) - 1)// 2])