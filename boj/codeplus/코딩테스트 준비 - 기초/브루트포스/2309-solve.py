"""
아홉명의 난쟁이
일곱난쟁이 키의 합이 100
아홉난쟁이의 키 => 일곱난쟁이 찾는 프로그램
키 - 100 안넘음, 모두 키가 다름
정답이 여러가지인경우 아무거나 오름차순으로 출력 
"""
from itertools import combinations

# 난쟁이 키 넣을 리스트 생성 
heights = []
# 9번 반복하면서
for _ in range(9):
    # 일곱난쟁의 키 한줄씩 입력 
    heights.append(int(input()))

# 9개의 키들중 순서 상관없이 7개 뽑는 조합 찾기
# 결과 조합 리스트 
result = []
# 각 조합들을 반복하면서
for  one_combi in list(combinations(heights, 7)):
    # 하나의 조합이 100이 되면 
    if sum(one_combi) == 100:
        # 현재 조합을 결과 조합리스트에 저장
        result = list(one_combi)
        # 반복 종료 
        break

# 결과 조합리스트 정렬
result.sort()
# 원소 하나씩 읽으며 한줄씩 출력 
for height in result:
    print(height)