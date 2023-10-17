"""
자연수만 존재. 모든 수 표현시 1, 2, 4만 사용
n : 자연수 
return : n을 124 나라에서 사용하는 숫자로 바꾼값 

1 = 0 * 3 + 1 => 1    2 = 0 * 2 + 2 => 2     3 = 1 * 3 + 0 => 4
---
4 = 1 * 3 + 1 => 11   5 = 1 * 3 + 2 => 12    6 = 2 * 3 + 0 => 14
---
7 = 2 * 3 + 1 => 21   8 = 2 * 3 + 2 => 22    9 = 3 * 3 + 0 => 24
---
10 = 3 * 3 + 1 => 41  11 = 3 * 3 + 2 => 42   12 = 4 * 3 + 0 => 44
---
13 = 4 * 3 + 1 => 111

3으로 나눈 나머지가 1일때 => 마지막 자리 수 1
3으로 나눈 나머지가 2일때 => 마자믹 자리 수 2
3으로 나눈 나머지가 0일때 => 마지막 자리 수 4 
3으로 나눈 몫에서 다시 3으로 나눈 나머지가 1일때 => 다음자리수 1
3으로 나눈 몫에서 다시 3으로 나눈 나머지가 2일때 => 다음자리수 2
3으로 나눈 몫에서 다시 3으로 나눈 나머지가 0일때 => 다음자리수 4
몫이 0보다 작을 때까지 반복
이때 나머지가 0일때면 몫은 -1 해줌 
나머지를 리스트에 삽입하고 반복이 끝났을때 숫자로 변환해주기 
"""
def solution(n):
    # 변환된 수의 각 자리수를 담는 리스트 converted_digits 빈 리스트로 초기화 
    converted_digits = [] 
    # 3으로 나눌 몫 target n으로 초기화 
    target = n 
    # target이 0보다 클 때까지 반복 진행
    while target > 0: 
        # target을 3으로 나눈 나머지 rest
        rest = target % 3
        # target을 3으로 나눈 몫 div
        div = target // 3
        # rest가 0이면
        if rest == 0: 
            # rest를 4로 변경
            rest = 4
            # div 1 감소
            div -= 1
        # rest를 converted_digits에 삽입 
        converted_digits.append(rest) 
        # target은 div로 변경 
        target = div 
    
    # converted_digits의 역순을 문자열로 합쳐서 리턴
    return ''.join(map(str, converted_digits[::-1]))