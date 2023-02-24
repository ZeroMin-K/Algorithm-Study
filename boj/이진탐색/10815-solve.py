"""
정수 하나가 적혀있는 숫자 카드 
숫자카드 N개 가짐. 정수 M개 주어졌을때 이 수가 적혀있는 숫자카드를 상근이가 가지고 있는지 확인

숫자카드를 입력받아 정렬
M개의 정수들을 하나씩 확인하면서 이진탐색으로 확인 

"""

import sys
input = sys.stdin.readline

# 숫자 카드 개수 (<= 500,000) 입력
n = int(input())

# 숫자카드에 적힌 정수 (-10000000보다 크거나 같고 10000000 작거나 같다)
cards = list(map(int, input().split()))
cards.sort()

# M (1<= M <= 500,000)
m = int(input())

# 숫자 카드인지 아닌지 정해야할 M개 정수 공백구분 (-10,000,000 <= 정수 <= 10,000,000)
data = list(map(int, input().split()))

def bisect(target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if cards[mid] == target:
            return True
        elif cards[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return False

result = [] 
for number in data:
    if bisect(number):
        result.append('1')
    else:
        result.append('0')

print(' '.join(result))