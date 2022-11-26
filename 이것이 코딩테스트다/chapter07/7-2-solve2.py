# n 입력
n = int(input())
# n 개의 정수 리스트 입력  - 가지고 있는 부품 리스트 parts => set로 변형
parts = set((map(int, input().split())))
# 정수 m 입력
m = int(input())
# m 개의 정수 리스트 입력 - 요청한 부품 리스트 requests
requests = list(map(int, input().split()))

# 요청한 부품 리스트 request 하나씩 탐색하며 
for request in requests:
    # request가 parts set안에 있으면
    if request in parts:
        # yes 출력
        print('yes', end =' ')
    # 없으면
    else:
        # no 출력 
        print('no', end=' ')