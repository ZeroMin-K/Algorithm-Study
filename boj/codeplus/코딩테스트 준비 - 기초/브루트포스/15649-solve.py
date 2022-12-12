from itertools import permutations

# 1뷰터 n까지의 자연수 중에서 중복없이 m개고른 길이가 m인 수열 
# n, m 입력 
n, m = map(int, input().split())

# 1부터 n까지의 자연수 리스트
arr = [i for i in range(1, n + 1)]

for permu_list in sorted(list(permutations(arr, m))):
    for num in permu_list:
        print(num, end =' ')
    print()