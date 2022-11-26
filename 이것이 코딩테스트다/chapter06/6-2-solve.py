# 수열 개수 n 입력
n = int(input())

array = []
# n번 반복하며
for _ in range(n):
    # 수 입력 
    array.append(int(input()))

# 내림차순 정렬
array.sort(reverse=True)

for elem in array:
    print(elem, end= ' ')