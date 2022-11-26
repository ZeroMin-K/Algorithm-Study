# n - 가게 부품 개수 입력
n = int(input())
# 가게 있는 전체 부품 번호 입력받아 집합 자료형에 기록
array = set(map(int, input().split()))

# m - 손님이 확인 요청한 부품 개수 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 호가인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end= ' ')
    else:
        print('no', end=' ')
