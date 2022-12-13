def find_sum(arr, n):
    global count 
    if sum(arr) == n:
        count += 1
        return 
    
    if sum (arr) > n:
        return 
    

    for i in [1, 2, 3]:
        arr.append(i)
        find_sum(arr, n)
        arr.pop()

# 테스트 케이스 개수 입력 
T = int(input())

# 테스트케이스 개수 만큼 반복하며
for _ in range(T):
    # 정수 n 입력 
    n = int(input())
    # 방법의 수 
    count = 0 
    # 합 리스트
    arr = []
    find_sum(arr, n)
    print(count) 