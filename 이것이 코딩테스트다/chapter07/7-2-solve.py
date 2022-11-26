"""
현재 가지고 있는 부품을 정렬
요청부품을 하나씩 확인하면서 이진탐색을 통해서  있는지 없는지 확인 가능 
"""
# n 입력
n = int(input())
# n 개의 정수 리스트 입력 - 가지고 있는 부품 리스트 parts
parts = list(map(int, input().split()))
# 부품리스트 정렬 
parts.sort()

# 정수 m 입력
m = int(input())
# m 개의 정수 리스트 입력 - 요청한 부품 리스트 requests
requests = list(map(int, input().split()))


# 이진 탐색 함수 - array, target
def binary_search(array, target, start, end):
    # start가 end보다 작거나 같은 동안 반복
    while start <= end:
        # 중간 인덱스 계산
        mid = (start + end) // 2

        # 중간인덱스의 원소와 target이 같으면
        if array[mid] == target:
            # 중간인덱스 반환
            return mid
        # 중간인덱스의 원소가 target보다 작으면
        elif array[mid] < target:
            # start는 mid + 1
            start = mid + 1
        # 중간 인덱스의 원소가 target보다 큰 경우 
        else:
            # end는 mid - 1
            end = mid - 1

    # 리스트안에 값이 없으면 -1 리턴 
    return -1


# 요청한 부품리스트 request하나씩 탐색하며
for request in requests:
    # 가지고있는 부품 리스트에서 이진탐색
    index = binary_search(parts, request, 0, len(parts) - 1)
    # 가지고 있으면 
    if index != -1: 
        # yes 출력
        print('yes', end=' ')
    # 없으면 
    else:
        # no 출력 
        print('no', end=' ')