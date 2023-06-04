def solution(X, Y):
    answer = ''
    
    # x 숫자들 등장하는 횟수 저장하는 리스트 - 길이 10, 값은 0으로 초기화
    x_list = [0] * 10 
    # y 숫자들 등장하는 횟ㅅ 저장하는 리스트 - 길이 10, 값은 0으로 초기화
    y_list = [0] * 10 
    
    # x를 하나씩 탐색하면서 - 원소 num
    for num in X:
        # num을 정수로 변환후 인덱스로 해서 x 등장 리스트에 1 증가
        x_list[int(num)] += 1
        
    # y를 하나씩 탐색하면서 - 원소 num
    for num in Y:
        # num을 정수로 변환후 인덱스로 해서 y 등장 리스트에 1 증가
        y_list[int(num)] += 1
        
    # 짝꿍 숫자들을 넣는 리스트
    pairs = [] 
    # 인덱스 i: 0부터 9까지 반복하면서
    for i in range(10):
        # 인덱스 i로 x와 y 등장리스트에서 둘다 0보다 클때 
        if x_list[i] > 0 and y_list[i] > 0:
            # x, y 등장 리스트 값 중에서 작은 것만큼 반복하여
            for _ in range(min(x_list[i], y_list[i])):
                # 인덱스 i를 짝꿍 리스트에 append
                pairs.append(i)
            
    # 짝꿍리스트의 길이가 0이면
    if len(pairs) == 0:
        # 짝꿍리스트는 -1만 원소로 가짐
        pairs = [-1]
    # 짝꿍리스트의 원소들의 합이 0이면
    elif sum(pairs) == 0:
        # 짝꿍리스트는 0만 원소로 가짐    
        pairs = [0]
    
    # 짝꿍리스트를 내림차순으로 정렬 후 문자로 변경후 join을 통해 문자열로 변환하기 
    return ''.join(list(map(str, sorted(pairs, reverse = True))))