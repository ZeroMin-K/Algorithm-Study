"""
arr : 0과 1로만 이루어진 정수 배열
arr을 이용해 새로운 배열 stk 만들기 
i의 초기값 0으로 설정. i가 arr의 길이보다 작으면 다음 반복
- stk가 빈 배열이면 arr[i]를 stk에 추가, i 1증가
- stk에 원소있고 
    - stk의 마지막원소가 arr[i]와 같으면 
        - stk 마지막 원소 제거. i에 1 증가
    - stk의 마지막 원소가 arr[i]와 다르면
        - stk맨마지막에 arr[i] 추가, i 1 증가
"""

def solution(arr):
    stk = []
    arr_length = len(arr)
    
    for i in range(arr_length):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    
    return stk if stk else [-1]