"""
0과 1로만 이루어진 문자열 s
모든 숫자를 전부 같게만들기
연속된 하나 이상의 숫자를 잡고 모두 뒤집기
0에서 1로, 1에서 0으로 바꾸는 것
행동 최소횟수 출력 

전부 1로 바꾸거나, 0으로 바꾸거나했을때 둘중 최소 횟수로 출력 
"""
s = input()
to_zero = 0
to_one = 0

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == '0':
            to_zero += 1
        else:
            to_one += 1

zero_s = s + '0'
if s[len(s) - 2] == '1':
    to_zero += 1

one_s = s + '1'
if s[len(s) - 2] == '0':
    to_one += 1

print(min(to_zero, to_one))