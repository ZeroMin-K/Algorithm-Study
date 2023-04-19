# n 을 문자열로 입력받아 리스트로 변경
n = list(input())
# n 길이의 절반만큼 슬라이싱하여 각 원소를 int로 변환
left = list(map(int, n[:len(n) // 2]))
# n 길이의 절반 인덱스부터 나머지까지 슬라이싱하여 각 원소를 int로 변환
right = list(map(int, n[len(n) // 2 :]))
# 둘이 같으면
if sum(left) == sum(right):
    # 'LUCKY' 출력
    print("LUCKY")
# 다르면 
else:
    # "READY" 출력 
    print("READY")