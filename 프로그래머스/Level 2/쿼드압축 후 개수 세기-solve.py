"""
arr : 0과 1로 이루어진 2^n x 2^n 크기의 2차원 정수 배열
쿼드트리 방식 압축
1. 압축하고자 하는 특정 영역S
2. S 내부에 있는 모든 수가 같은값이면 S를 해당 수 하나로 압축
3. 그렇지않다면 S를 정확히 4개의 균일한 정사각형 영역으로 쪼갠 뒤
    각 정사각형 영역에 대해 같은 방식 압축 시도
return : arr 압축했을때 최종적으로 남는 0의 개수, 1의 개수를 담은 배열 
"""

def solution(arr):
    # 0과 1의 개수 담는 리스트 numbers. 인덱스 0 : 0의 개수, 인덱스 1 : 1의 개수 
    numbers = [0, 0]
    
    """
    dfs함수 선언 
    현재 길이에서 시작위치에서 끝위치까지 압축가능한지 확인, 불가능하면 길이 줄여서 탐색
        Args: 
            현재 길이 n, 시작위치 start_x, start_y, 끝 위치 end_x, end_y 
        Return: None 
    """
    def dfs(n, start_x, start_y, end_x, end_y): 
        # 시작위치의 숫자값 start는 arr[start_x][start_y] 값
        start = arr[start_x][start_y]
        # 현재 길이 n이 1이면
        if n == 1: 
            # numbers[start] 1 증가 
            numbers[start] += 1
            # 리턴 
            return 
            
        # 현재 압축 가능한지 여부 compressed True 초기화
        compressed = True 
        # 인덱스 i : start_x부터 end_x - 1 까지 반복 
        for i in range(start_x, end_x): 
            # 인덱스 j: start_y부터 end_y - 1 까지 반복
            for j in range(start_y, end_y):
                # start와 arr[i][j]가 다르면
                if start != arr[i][j]:
                    # compressed False로 변경
                    compressed = False
                    # break
                    break
                
        # compressed가 True이면 (압축 가능하면)
        if compressed: 
            # numbers[start] 1 증가 
            numbers[start] += 1
        # 압축 불가능하면
        else: 
            # n을 n// 2함
            n //= 2
            # << 현재 리시트를 4등분하여 탐색 >> 
            # dfs 호출 : 인자 n, start_x, start_y, start_x + n, start_y + n
            dfs(n, start_x, start_y, start_x + n, start_y + n)
            # dfs 호출 : 인자 n, start_x, start_y + n, start_x + n, end_y
            dfs(n, start_x, start_y + n, start_x + n, end_y)
            # dfs 호출 : 인자 n, start_x + n, start_y, end_x, start_y + n
            dfs(n, start_x + n, start_y, end_x, start_y + n)
            # dfs 호출 : 인자 n, start_x + n, start_y + n, end_x, end_y 
            dfs(n, start_x + n, start_y + n, end_x, end_y)
    
    # n : arr의 길이 
    n = len(arr)
    # dfs 호출 : 인자 n, 0, 0, n, n
    dfs(n, 0, 0, n, n )
    # numbers 리턴 
    return numbers