# n, m을 공백으로 구분하여 입력
n, m = map(int, input().split())

result = 0
# 한줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 들 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)