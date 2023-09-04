"""
S : 각 자리가 숫자 (0부터 9)로만 이루어진 문자열 
왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하여 숫자 사이 x, +연산자 넣어 만들 수 있는 가장 큰 수 구하기 
왼쪽에서부터 순서대로 계산
최대한 곱하기 사용하기 
현재 숫자가 0이거나 다음숫자가 0이거나 다음 숫자가 1이면 곱하는것보다는 더하기 
"""

s = input()
result = 0

for num in list(map(int, s)):
    if result <= 1 or num <= 1: 
        result += num
    else:
        result *= num 

print(result)