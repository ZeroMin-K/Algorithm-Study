# n 입력
from re import L


n = int(input())

# n개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 기본 정렬라이브러리 이용하여 정렬수행
array = sorted(array, reverse = True)

# 정렬이 수행된 결과 출력
for i in array:
    print(i, end=' ')