"""
주어진 수들을 M번을 더하여 가장 큰수를 만드는 법칙
배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과 불가
서로 다른 인덱스의 수가 같아도 서로 다른 수 

정렬을 해서 가장 큰수를 k번 더하고 그다음 수를 더하고를 반복해서 m번 동안 진행 
총 k + 1 크기의 수열이 생기고 이게 몇번 반복하는지 
나머지는 가장 큰수로 더하기 
"""

# n, m, k 입력 
n, m, k = map(int, input().split())
# n개의 자연수 리스트 입력 
data = list(map(int, input().split()))

# 리스트 정렬 
data.sort(reverse = True)

# 첫번째수 = 가장 큰수 
first = data[0]
# 두번째수 = 가장 큰수의 다음 수 
second = data[1]

# k+1을 몇번 반복해야하는지 m 에서 k + 1 몫 구함
repeat = m // (k + 1) 
# m에서 k + 1로 나눌때 나머지 구함
rest = m % (k + 1) 

# 최종 수는 몫 * (가장 큰 수 * k + 그다움수) + 나머지 * 가장 큰수 
result = repeat * (first * k + second) + rest * first

print(result)