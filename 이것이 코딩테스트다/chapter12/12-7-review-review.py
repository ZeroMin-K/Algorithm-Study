"""
점수 n을 자릿수 기준으로 반으로 나누어 왼쪽부분의 합과 오른쪽 부분 각 자리수합이
동일할 경우 LUCKY 다르면 READY 
리스트 슬라이싱과 int를 이용하여 풀이 진행 
"""

# n을 문자열로 입력
n = input() 
# n의 왼쪽부분을 슬라이싱하여 map을 통해 int로 변환 후 sum 구하기
left = sum(map(int, n[:len(n) // 2]))
# n의 오른쪽부분을 슬라이싱하여 map을 통해 int로 변환 후 sum 구하기ㅜ
right = sum(map(int, n[len(n) // 2:]))

# 둘이 같으면
if left == right:
    # LUCKY 출력
    print("LUCKY")
# 다르면
else:
    # READY 출력 
    print("READY")