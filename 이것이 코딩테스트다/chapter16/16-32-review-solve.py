"""
위층부터 시작해서 아래층으로 내려올때 선택된 수의합이 최대가 되는 경로 구함
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽또는 대각선 오른쪽에 있는것중에서만 선택

대각선 왼쪽 : -1행 -1열
대각선 오른쪽: -1행 같은열 
현재 수의합이 최대이려면 대각선 왼쪽, 대각선 오른쪽 중 최대를 찾아서 더함

현재 열이 [0]이면 => 가장 왼쪽이면 왼쪽에서 오는거 없음 
현재 열이 행과 같으면 => 가장 오른쪽이기때문에 오른쪽에서 오는 거없음 

"""

# 삼각형의 크기 n 입력
n = int(input())
# 삼각형 리스트 빈 리스트로 초기화 
triangle = [] 
# n번 반복하면서
for _ in range(n):
    # 공백 구분으로 숫자들을 리스트로 입력하여 삼각형 리스트에 append
    triangle.append(list(map(int, input().split())))
    
# 인덱스 i - 1부터 n - 1까지 반복하면서 
for i in range(1, n):
    # 인덱스 j - 0부터 삼각형리스트[i]의 길이 - 1 까지 반복하면서
    for j in range(len(triangle[i])):
        # 현재 j가 0이면 
        if j == 0:
            # 오른쪽에서 오는거만 더함
            triangle[i][j] += triangle[i-1][j]
        # 현재 j가 i와 같으면 
        elif j == i: 
            # 왼쪽에서 오는거만 더함 
            triangle[i][j] += triangle[i-1][j-1]
        # 나머지 경우에는 
        else:
            # 현재 최대합은 왼쪽에서오는거, 오른쪽에서 오는거 중 최대값을 더함 
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
# 삼각형 리스트 n-1 줄에서 가장 큰값을 출력 
print(max(triangle[n-1]))