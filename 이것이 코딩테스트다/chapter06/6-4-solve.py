"""
두 배열 A, B  n개의 원소로 구성, 모두 자연수
최대 K번 바꿔치기 연산 => 배열 A의모든 원소 합이 최대가 되도록
배열 a 오름차순으로 정렬
배열 b를 내림차순으로 정렬
k번 반복하면서 배열 a 원소보다 배열 b원소가 더 크면 교환 
배열 a는 오름차순으로 정렬되어 배열b원소보다 더 크는 순간 더 탐색할 필요없음. 
"""

# n, k 공백으로 구분되어 입력
n, k = map(int, input().split())

# 배열 a 원소 공백으로 구분되어 입력
a = list(map(int, input().split()))

# 배열 b 원소 공백으로 구분되어 입력 
b = list(map(int, input().split()))

# 배열 a 오름차순으로 정렬
a.sort()
# 배열 b 내림차순으로 정렬
b.sort(reverse = True) 


# k번 반복하면서 
for i in range(k):
    # a[i]가 b[i]보다 작으면
    if a[i] < b[i]: 
        # a[i], b[i] 교환 
        a[i], b[i] = b[i], a[i] 
    # a[i]가 b[i]보다 크면 교환할 필요 없음. 
    else: 
        break

# 배열 a 합 출력
print(sum(a))