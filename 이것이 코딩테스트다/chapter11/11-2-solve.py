"""
문자열 s: 각 자리가 숫자(0부터9)로만 이루어진 문자열
왼쪽부터 오른쪽으로 하나씩 모든 숫자 확인하며
숫자 사이에 x, +연산자 넣어 결과적으로 만들 수 있는 가장 큰 수 구하기
모든 연산은 왼쪽에섭터 순서대로 이루어진다고 가정

문자열을 하나씩 읽으면서
다음수가 0이거나 1이면 +를 
나머지는 곱하기 하기 

"""

# 문자열 입력
s = input()
# 첫번째 문자열을 정답 answer에 넣어 초기화
answer = int(s[0]) 
# 인덱스 i - 1부터 문자열 길이 - 1까지 반복하면서
for i in range(1, len(s)):
    # 현재 숫자는 문자열[i]를 int로 변환
    number = int(s[i])
    # answer나 현재 숫자가 0이거나 1이면
    if answer == 0 or answer == 1 or number == 0 or number == 1:
        # answer에 현재숫자를 더함
        answer += number
    # 나머지는
    else:
        # answer에 현재 숫자를 곱함
        answer *= number
        
# 정답 answer 리턴
print(answer)