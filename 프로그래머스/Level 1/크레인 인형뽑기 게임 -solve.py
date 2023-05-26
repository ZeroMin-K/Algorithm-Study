"""
1 * 1 크기의 칸들로 이루어진 N * N 크기 정사각 격자
각 격자에 인형이 1*1크기로 한칸 차지있, 인형이 없으면 빈칸
인형은 가장아래칸부터 차곡차곡 쌓임 
크레인을 좌우로 움직여서 멈춘 위치 가장 위 인형을 집어올려 
바구니의 아래칸부터 인형이 순서대로 쌓임 
같은 모양의 인형 두개가 바구니에 연속해서 쌓이면 바구니에서 두 인형 사라짐
인형이 없는곳에서 크레인 작동시 아무런 일도 일어나지 않음 
board: 격자 상태 담긴 2차원배열
moves: 크레인 작동시킨 위치 
크레인 모두 작동시킨후 터트려져 사라진 인형 개수 리턴

moves를 탐색하면서 크레인 작동시켜 바구니를 스택으로 사용하여 옮김
바구니 스택의 마지막과 현재 이동시키는 인형이 같으면
바구니 스택을 pop하고, 인형 두개 개수 카운트 

크레인은 열로 움직이니까 해당 열의 row를 0부터 반복하면서 0이 아니면
해당 인형을 빼내는 것 
"""

def solution(board, moves):
    # 터트려 사라진 인형의 개수 
    answer = 0
    # board의 크기 n 
    n = len(board)
    # 인형 바구니 basket 빈 리스트로 초기화 
    basket = [] 
    
    # moves를 하나씩 탐색하면서 - 원소 move(크레인의 열 위치)
    for move in moves: 
        # 크레인의 위치 (1부터 시작하므로 -1)
        col = move - 1
        
        # 인덱스 i : 0부터 n -1만큼반복하면서
        for i in range(n):
            # board의 i행 col열이 0이 아니면
            if board[i][col] != 0:
                # 바구니가 비어있지 않고 board의 i행 col열의 인형과 바구니의 마지막 인형이 같으면
                if len(basket) > 0 and board[i][col] == basket[-1]:
                    # 바구니 pop
                    basket.pop()
                    # 사라진 인형개수 2 증가 
                    answer += 2
                # 다르면 
                else:
                    # 바구니의 인형 넣기 append
                    basket.append(board[i][col])
                    
                # board의 i행 move열을 빈공간으로 바꿈 
                board[i][col] = 0 
                
                # 크레인은 행에서 이동을 멈추고 다음 열로 이동
                break

    return answer