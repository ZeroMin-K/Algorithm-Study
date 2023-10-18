"""
서로 다른 k개의 수를 저장한 배열 만들기 
일정한 범위내에서 무작위로 수를 뽑은 후 지금까지 나온적이 없는 수이면 배열 맨뒤에 추가
어떤수가 무작위로 주어질지 알고있따고 가정
실제 만들어질 길이 k의 배열 예상
arr: 정수 배열
return : 무작위수는 arr에 저장된 순서대로 주어질 예정. 완성된 배열 
    - 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1 로 채워서 리턴 
"""

def solution(arr, k):
    answer = []
    for num in arr:
        if num in answer: continue
        
        answer.append(num)
        if len(answer) == k:
            break 
    
    while len(answer) < k:
        answer.append(-1)
    
    return answer