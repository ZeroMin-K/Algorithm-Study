"""
정수 삼각형
맨 위층에서부터 시작해서 아래에 있는 수중 하나 선택하여 아래층 내려올때 
선택된 수의 합이 최대가 되는 경로 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는것만
7 
3 8 
8 1 0 
2 7 4 4 
4 5 2 6 5

현재 층에서 최대 값은 대각선왼쪽, 대각선 오른쪽 중 최대값 + 현재 값
대각선 왼쪽 => 이전 행, 이전 열
대각선 오른쪽 => 이전 행, 같은 열 
맨 대각선 왼쪽일 때 왼쪽에서 오는거 없음 => 현재열이 0일때
맨 대각선 오른쪽일 때 오른쪽에서 오는 거 없음 => 현재 열이랑 행이 같을 때 
"""

# 빠른 입력
import sys
input = sys.stdin.readline
# 삼각형 크기 n 입력 
n = int(input()) 
# 삼각형의 숫자 담는 tri 리스트 생성
tri = [] 
# n번 반복하면서
for _ in range(n): 
    # 한줄 입력해서 tri에 삽입
    tri.append(list(map(int, input().split())))
    
# 인덱스 i: 1부터 n - 1까지 반복하면서
for i in range(1, n): 
    # 인덱스 j: 0부터 tri[i]의 길이 - 1 까지 반복하면서
    for j in range(len(tri[i])): 
        # 대각선 왼쪽에서 오는 값 left. j가 0이면 0 아니면 tri[i - 1][j - 1]
        left = 0 if j == 0 else tri[i - 1][j - 1] 
        # 대각선 오른쪽에서 오는 값 right. j가 i와 같으면 0. 아니면 tri[i - 1][j]
        right = 0 if i == j else tri[i - 1][j] 
        # tri[i][j]는 left, right중 큰값을 더함
        tri[i][j] += max(left, right) 
        
# tri[n - 1]중 큰값 출력 
print(max(tri[n - 1]))