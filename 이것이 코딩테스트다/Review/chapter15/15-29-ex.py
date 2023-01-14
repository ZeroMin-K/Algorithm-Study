# 집의 개수 n, 공유기 개수 c 입력
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보 입력
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()        # 이진 탐색 수행을 위한 정렬 수행

start = 1                   # 가능한 최소 거리 
end = array[-1] - array[0]  # 가능한 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2        # mid는 가장 인접한 두 공유기 사이의 거리 의미
    value = array[0]
    count = 1
    # 현재 mid값을 이용해 ㅁ공유기 설치
    for i in range(1, n):       # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:      # c개 이상의 공유기를 설치할 수 있는 경우 거리 증가
        start = mid + 1
        result = mid        # 최적의 결과 저장
    else:   # c개 이상의 공유기를 설치할 수 없는 경우 거리감소
        end = mid - 1

print(result) 