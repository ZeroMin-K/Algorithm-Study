"""
알파벳 대문자와 숫자로만 구성된 문자열 입력
모든 알파벳을 오름차순 정렬 출력, 모든 숫자 더한값을 이어 출력 

문자열을 하나씩 탐색하면서 문자면 문자 리스트에 넣고
숫자면 계속 더함
문자리스트를 정렬해서 문자열로 바꾼후 숫자를 문자로 바꿔서 문자열에 붙여줌 
"""

# 문자열 s 입력
s = input()

# 문자 리스트 alphas 빈 리스트로 초기화 
alphas = [] 
# 숫자 합 total = 0
total = 0 

# 문자열 s 하나씩 탐색하면서 - word
for word in s: 
    # word가 문자면
    if word.isalpha(): 
        # alphas에 append
        alphas.append(word)
    # 숫자면
    else:
        # 숫자로 바꾼후 total에 더해줌
        total += int(word)

# 문자 리스트 alphas 정렬
alphas.sort() 
# alphas를 하나의 문자열로 변환 answer
answer = ''.join(alphas)
# answer에 문자열로 바꾼 total을 붙여줌
answer += str(total)
# answer print 
print(answer)