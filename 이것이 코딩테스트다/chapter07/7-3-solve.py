"""
절단기 높이 H 지정 - 높이가 h보다 긴 떡은 H위 부분이 잘림
낮은 떡은 잘리지 않음  잘린떡의 나머지를 손님이 가져감
요청한 길이가 M일때 적어도 m만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값 설정
h가 작아질수록 나머지 부분이 커짐
h가 클수록 나머지부분이 작아짐. 
이진탐색을 이용해 최소 m길이를 가져갈 수 있는 h최대 높이 찾기 
"""

# 떡의 개수 n, 떡의 길이 m 입력
n, m = map(int, input().split())
# 떡의 개별높이가 공백을 기준으로 입력 
heights = list(map(int, input().split()))

# 시작 떡 길이 = 0
start = 0
# 마지막 떡길이 = 떡중에서 가장 큰 떡 길이 
end = max(heights)

max_height = 0
# 시작떡길이가 마지막떡 길이보다 작은 동안 반복
while start <= end: 
    # 중간 높이 길이 h 는 시작 떡길이 + 마지막 떡길이 / 2
    h = (start + end) // 2
    # 현재에서 떡길이 합 - 각 떡들을 반복하면서 h만큼 잘라낸만큼 길이 더함 
    current_sum = sum([height - h for height in heights if height - h > 0 ])

    # 현재 떡길이 합이 m보다 작으면 => 절단기 높이 낮추기 
    if current_sum < m:
        # 마지막 떡길이를 중간높이 길이 -1 로 설정
        end = h - 1
    # 현재 떡길이 합이 m보다 크면 => 절단기 높이 올리기 
    else: 
        # 시작 떡길이를 중간높이 길이 + 1 로 설정 
        start = h + 1
        max_height = max(max_height, h)

# 최대 높이 출력
print(max_height)
