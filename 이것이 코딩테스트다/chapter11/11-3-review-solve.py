"""
문자열 s: 0과 1로만 이루어짐. 모든 숫자를 전부 같게 만들기
s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것
0 -> 1, 1 -> 0 

전부 0으로 만들때 뒤집는 횟수, 전부 1로 만들때 뒤집는 횟수 비교하여
적은 횟수를 출력 

0 -> 1로 바뀌면 1로 바꿀때 횟수 증가
1 -> 0로 바뀌면 0로 바꿀때 횟수 증가 
"""

# 문자열 s입력
s = input() 

# 전부 0으로 만들때 뒤집는 횟수 to_zero 0으로 초기화 
to_zero = 0
zero_s = s + '0'

# 전부 1로 만들때 뒤집는 횟수 to_one 0으로 초기화 
to_one = 0
one_s = s + '1'
        
for i in range(1, len(zero_s)):
    # 문자열 s가 현재 인덱스 i에 해당하는 문자가 0이고 이전 인덱스 문자가 1이면 
    if zero_s[i-1] == '1' and zero_s[i] == '0':
        # 0으로 바뀔때 횟수 증가
        to_zero += 1
        
for i in range(1, len(one_s)):
    # 이전 인덱스 문자가 0이고 현재 인덱스 i에 해당하는 문자가 1이면
    if one_s[i-1] == '0' and one_s[i] == '1':
        # 1로 바뀔때 횟수 증가 
        to_one += 1

# 전부 0으로 만들때 뒤집는 횟수 to_zero, 전부 1로 만들때 뒤집는 횟수 to_one 중 가장 작은 수 출력 
print(min(to_zero, to_one))