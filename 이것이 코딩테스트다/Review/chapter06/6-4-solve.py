# n, k 공백으로 구분하여 입력
n, k = map(int, input().split())

# 배열 a 원소 공백으로 구분하여 입력
a = list(map(int, input().split()))

# 배열 b 원소 공백으로 구분하여 입력
b = list(map(int, input().split()))

# 배열 a 오름차순 정렬
a.sort()
# 배열 b 내림차순 정렬
b.sort(reverse = True)

# k번 반복하며
for i in range(k):
    # a[i]가 b[i]보다 작으면
    if a[i] < b[i]:
        # a[i], b[i] 교환
        a[i], b[i] = b[i], a[i]
    # a[i]가 b[i]보다 크면 교환X
    else:
        break

# 배열 a합 출력
print(sum(a))