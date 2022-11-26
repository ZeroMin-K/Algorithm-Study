# n, k 입력 
n, k = map(int, input().split())   
# 배열 a 모든 원소 입력  
a = list(map(int, input().split()))
# 배열 b 모든 원소 입력 
b = list(map(int, input().split()))

# 배열 a 오름차순 정렬 
a.sort()
# 배열 b 내림차순 정렬 
b.sort(reverse = True) 

# 첫번째 인덱스부터 확인. 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # a의 원소가 b원소보다 작은 경우 
    if a[i] < b[i]:
        # 두 원소 교체
        a[i], b[i] = b[i], a[i]
    # a의 원소가 b의 원소보다 크거나 같을때 반복문 탈출
    else:
        break

# 배열 a의 모든 원소 합 출력 
print(sum(a))