"""
길이가 같은 배열 a, b 두개. 자연수로 이루어짐.
배열 a, b에서 각각 한개 숫자 뽑아 두 수 곱함. 배열 길이만큼 반복하며 두수를 곱한 값을 누적하여 더함
최종적으로 누적된 값이 최소가 되도록 만들기. 
각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없음. 

1 2 4 // 5 4 4. 4 4 5 // 4 2 1
1 2 // 4 3. 3 4 // 2 1

return : 최종적으로 누적된 최솟값 

하나는 오름차순 정렬, 하나는 내림차순 정렬하여 첫번째부터 하나씩 곱하면서 누적하기 

"""


def solution(A,B):
    result1 = 0 
    # a를 오름차순, b를 내림차순으로 정렬했을 때 누적합
    A.sort()
    B.sort(reverse = True)
    for a, b in zip(A, B): 
        result1 += a * b
    
    result2 = 0
    # a를 내림차순, b를 오름차순으로 정렬햇을때 누적합
    A.sort(reverse = True)
    B.sort()
    for a, b in zip(A, B):
        result2 += a * b

    # 누적합 중 최소값리턴 
    return min(result1, result2)