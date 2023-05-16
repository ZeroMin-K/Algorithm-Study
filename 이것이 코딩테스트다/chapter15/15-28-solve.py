"""
고정점: 수열의 원소 중 그 값이 인덱스와 동일한 원소 
수열 n개, 서로 다른 원소, 오름차순 정렬
고정점이 있다면 고정점 출력 
없다면 -1 출력 

logN으로 설계 => 이진탐색을 이용해서 인덱스와 원소 비교하기 
"""

# n 입력
n = int(input())
# n개의 원소 정수 형태로 공백 구분으로 리스트에 입력
data = list(map(int, input().split()))

# 고정점은 -1 (고정점이 없는것을 가정)
fixed_point = -1
# 이진탐색 진행
# 시작 인덱스 start = 0
start = 0 
# 끝 인덱스 end = n - 1
end = n - 1
# 시작 인덱스가 끝 인덱스보다 작거나 같을때까지 반복 진행
while start <= end: 
    # 중간 인덱스 mid  = 시작인덱스 start + 끝 인덱스  end // 2
    mid = (start + end) // 2
    # 중간인덱스 mid와 mid에있는 원소가 같으면 
    if mid == data[mid]:
        # 고정점은 mid
        fixed_point = mid
        # 반복 종료 
        break
    # 중간 인덱스 mid보다 mid에 있는 원소가 크면 
    elif mid < data[mid]:
        # 왼쪽 탐색 
        # 끝인덱스 end = mid - 1
        end = mid - 1
    # 중간 인덱스 mid보다 mid에 있는 원소가 작으면
    else:
        # 오른쪽 탐색
        # 시작 인덱스 start = mid + 1
        start = mid + 1

# 고정점 출력
print(fixed_point)