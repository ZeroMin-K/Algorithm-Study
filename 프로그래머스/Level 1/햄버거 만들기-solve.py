"""
재료를 조리된 순서대로 상수 앞에 아래서부터 위로 쌓음. 순서에 맞게 쌓여서 포장
빵 - 야채 - 고기 - 빵 순. 재료의 높이는 무시.
빵: 1, 야채: 2, 고기: 3
스택을 이용하여 풀이
빵, 야채, 고기, 빵 (1, 2, 3, 1) 이되면 pop해서 햄버거 개수 증가 
"""
def solution(ingredient):
    # 햄버거 개수 
    answer = 0
    # 햄버거 쌓는 스택 리스트 stack 빈 리스트로 초기화
    stack = [] 
    # ingredient 하나씩 탐색하면서 - 원소 i
    for i in ingredient: 
        # 현재 재료 i를 리스트에 삽입
        stack.append(i) 
        # 현재 스택 리스트의 길이가 4이상이면
        if len(stack) >= 4: 
            # 스택리스트를 끝에서 4개까지 슬라이싱했을때 [1, 2, 3, 1] 이 되면
            if stack[-4:] == [1, 2, 3, 1]:
                # 햄버거 개수 증가
                answer += 1
                # 스택 리스트 pop 4번 진행 
                for _ in range(4):
                    stack.pop()

    return answer