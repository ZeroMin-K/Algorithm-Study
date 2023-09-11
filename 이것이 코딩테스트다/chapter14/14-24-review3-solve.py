"""
특정 위치의 집에 한개 안테나 설치
모든 집까지 거리의 총합이 최소가 되도록 
안테나를 설치할 위치 선택 

정렬 후 중간위치에다 설치 
"""
# 집의 수 n 입력
n = int(input()) 
# 집 위치 houses 리스트로 입력
houses = list(map(int, input().split()))
# houses 정렬
houses.sort() 
# houses의 중간값 출력 
print(houses[(len(houses) - 1 ) // 2])