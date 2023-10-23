"""
고정점: 원소 중 그값이 인덱스와 동일한 원소 
n개의 서로 다른 원소 포함한 하나의 수열. 오름차순 정렬
고정점출력. 없다면 -1 
"""
n = int(input())
data = list(map(int, input().split()))

start = 0
end = len(data) - 1

fixed_point = -1 
while start <= end:
    mid = (start + end) // 2
    
    if mid == data[mid]:
        fixed_point = mid
        break 
    elif mid < data[mid]:
        end = mid - 1
    else:
        start = mid + 1
        
print(fixed_point)