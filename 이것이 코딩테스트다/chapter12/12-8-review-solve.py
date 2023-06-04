"""
알파벳 대문자, 숫자(0 ~ 9)로만 구성된 문자열 입력
오름차순으로 정렬하여 출력한뒤 모든 숫자를 더한 값을 이어서 출력

문자열을 하나씩 읽으면서 알파벳이면 리스트에 따로 저장.
숫자면 따로 숫자값을 더하고 알파벳만 저장한 리스트를 정렬하고 
문자열로 만든다음 숫자를 뒤에 붙여줌 

"""

# 문자열 s 입력
s = input()

# 알파벳만 담는 리스트
alphas = [] 

# 숫자의 합을 담는 값 total 0 으로 초기화 
total = 0
# 문자열 s를 하나씩 읽으면서 - 원소 word
for word in s:
    # word가 알파벳이면
    if word.isalpha():
        # 알파벳만 담는 리스트에 append
        alphas.append(word)
    # 나머지의 경우 (숫자이면)
    else:
        # 정수형으로 변환후 숫자합에 더해주기
        total += int(word)
        
# 문자열리스트를 정렬후 문자열로 변환
answer = ''.join(sorted(alphas))
# 숫자의 합이 0보다 크면 
if total > 0:
    # 문자열에 숫자를 문자로 변경후 붙여줌
    answer += str(total)
    
# 정답 문자열 출력 
print(answer)