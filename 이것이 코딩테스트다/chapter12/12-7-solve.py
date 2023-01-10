# 현재 점수 N. 자릿수는 항상 짝수형태 
# 자릿수를 기준으로 반으로 나누어 
# 왼쪽 부분의 각 자리수 합과 오른쪽 부분 각 자릿수 합을 더한값이 동일할때
# 사용가능하면 LUCKY, 불가능하면 READY
# 0123 => 01,23 => 0 ~ len / 2 - 1, len / 2 ~ 나머지

# n을 리스트로 입력
data = list(map(int, input()))

# 왼쪽 부분 절반
head = data[:len(data) // 2]

# 오른쪽 부분 절반
tail = data[len(data) // 2:]

# 왼쪽 부분 각 자리수 합과 오른쪽 부분 각 자리수 합이 같을 때
if sum(head) == sum(tail):
    print("LUCKY")
else:
    print("READY")