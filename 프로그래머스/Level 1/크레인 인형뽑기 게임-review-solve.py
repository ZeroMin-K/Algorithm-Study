"""
n * n 정사각 격자 게임화면. 격자칸에 인형, 없는 칸은 빈칸 
크레인을 좌우로 움직여 멈춘 위 가장 위에 있는 인형 집어올림
집어올린 인형은 바구니에 가장 아래칸부터 쌓임
같은 모양 인형 두개가 바구니에 연속으로 쌓이면 두인형은 터뜨려져서 사라짐
크레인이 인형없는곳에 가면 아무일도 안 일어남. 바구니는 충분히 큼.
board: 게임 화면 격자 상태 담긴 2차원 배열
    - 0: 빈칸, 1 ~ 100: 인형 
moves: 크레인 작동 위치
    - 가로로 이동 
    - 1부터 시작이라 -1 진행하기 
return: 터뜨려져 사라진 인형 개수 

바구니를 스택으로 구현하여 크레인 작동시켜
바구니 스택에 두개 쌓이면 pop해서 개수를 카운트하여 리턴 

"""

def solution(board, moves):
    # 사라진 인형의 개수 
    answer = 0
    # board의 길이 n
    n = len(board)
    # 바구니 스택 리스트 stack 
    stack = [] 
    
    # moves를 하나씩 탐색하면서 - 원소 move
    for move in moves: 
        # 크레인 위치 - loc은 move - 1
        loc = move - 1
        # 인덱스 i - 0부터 n - 1까지 반복하면서 : 크레인은 loc열에서 행만 이동 
        for i in range(n):
            # board[i][loc]가 0보다 크면 => 인형 발견
            if board[i][loc] > 0: 
                # board[i][loc] 값을 stack에 append
                stack.append(board[i][loc]) 
                # board[i][loc]값은 0. 인형 없어짐 
                board[i][loc] = 0
                # 현재 크레인 이동 종료 
                break
        # stack의 길이가 2보다 클때 
        if len(stack) >= 2: 
            # stack의 가장 마지막 원소와 stack의 마지막 두번째 원소가 같으면
            if stack[-1] == stack[-2]:
                # stack에서 pop두번 진행
                stack.pop()
                stack.pop()
                # 사라진 인형의 개수 2 증가 
                answer += 2
            
    return answer