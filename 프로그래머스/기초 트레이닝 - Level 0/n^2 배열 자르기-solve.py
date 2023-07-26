"""
1차원 배열 생성
1. n행 n열 크기 비어있는 2차원 배열 생성
2. i를 1부터 n번까지 반복하면서
    - 1행 1열부터 i행 i열까지 i로 채움
3. 1행부터 n행까지 잘라내어 모두 이어붙인 새로운 1차원배열만듬
4. 새로운 1차원 배열 arr에 대해 arr[left], arr[left + 1]부터 arr[right]만 남기고 지우기
return : 만들어진 1차원 배열 
"""

def solution(n, left, right):
    return [max(k // n, k % n) + 1 for k in range(left, right + 1)]