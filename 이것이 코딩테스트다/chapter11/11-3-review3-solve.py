"""
s : 0과 1로만 이루어진 문자열
문자열 s에 있는 모든 숫자를 전부 같게 만들기
s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
1을 0으로, 0을 1로 
해야하는 행동 최소 횟수 출력 
"""
s = input()
to_zero = 0 
to_one = 0 

all_one = s + '1' 
all_zero = s + '0'

for i in range(len(all_one) - 1):
    if all_one[i] == '0' and all_one[i + 1] == '1':
        to_one += 1

for i in range(len(all_zero) - 1):
    if all_zero[i] == '1' and all_zero[i + 1] == '0':
        to_zero += 1

print(min(to_zero, to_one))