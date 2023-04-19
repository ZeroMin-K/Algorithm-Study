"""
점수 n - n을 자릿수 기준으로 반으로 나누어 왼쪽부분 각 자릿수합, 오른쪽부분 각 자리수합 같으면
LUCKY, 아니면 READY 출력 
항상 짝수 자릿수의 n
n을 문자열 원소 리스트로 바꾸어서 절반만큼 슬라이싱하여 각 원소를 int로 바꾸후 
리스트의 합 비교해서 확인하기 
"""

# n 입력
n = int(input())
# n 을 문자열로 바꾸고 리스트로 바꾸고
n = list(str(n))
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