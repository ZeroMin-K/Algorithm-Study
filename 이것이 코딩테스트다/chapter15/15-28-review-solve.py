"""
고정점: 원소 중에서 값이 인데스와 동일한 원소
수열에 n개 서로 다른 원소 오름차순 정렬 
고정점이 있다면 고정점 출력
최대 1개만 존재 없으면 -1 

이진탐새을 이용해서 원소값과 인덱스를 비교하면서 탐색진행
"""

# n 입력
n = int(input())
# n개의 원소 공백으로 구분해서 리스트로 입력
data = list(map(int, input().split()))

# 이진 탐색 진행
# 시작점 start = 0으로 초기화 
start = 0
# 끝점 end = n - 1으로 초기화
end = n - 1

# 현재 고정점은 -1 
fixed_point = -1 
# 시작점 start가 끝점 end보다 작거나 같을때까지 반복진행하면서
while start <= end: 
    # 중간점 mid는 start와 end를 더한후 2로 나눈값
    mid = (start + end) // 2
    # mid에 있는 값이 mid와 같으면
    if data[mid] == mid:
        # mid가 고정점
        fixed_point = mid
        break
    # mid에 있는값이 mid보다 작으면
    elif data[mid] < mid:
        # 오른쪽 탐색
        # start는 mid + 1
        start = mid + 1
    # 나머지 경우 (mid에 있는 값이 mid보다 크면)
    else:
        # 왼쪽 탐색
        # end = mid - 1
        end = mid - 1
        
# 고정점 출력 
print(fixed_point)