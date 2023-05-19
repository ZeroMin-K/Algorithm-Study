def solution(X, Y):
    answer = ''
    
    # 짝꿍리스트 pairs 빈 리스트 로 초기화
    pairs = [] 
    
    # x에서 0부터 9까지 총 몇번씩 등장하는지 세는 리스트 초기화 x_count 
    x_count = [0] * 10 
    # y에서 0부터 9까지 총 몇번씩 등장하는지 세는 리스트 초기화 y_count
    y_count = [0] * 10 
    
    # x하나씩 읽으면서 
    for num in X:
        # x의 숫자만큼 x_count 증가하기
        x_count[int(num)] += 1
        
    # y하나씩 읽으면서
    for num in Y:
        # y의 숫자만큼 y_count 증가하기 
        y_count[int(num)] += 1
    
    # 인덱스 i: 0부터 9까지 읽으면서
    for i in range(10):
        # x_count, y_count 둘다 1이상이면
        if x_count[i] >= 1 and y_count[i] >= 1:
            # x_count, y_count중 작은거만큼
            for _ in range(min(x_count[i], y_count[i])):
                # pairs에 i를 append
                pairs.append(i)

    # 짝꿍리스트가 비어있으면
    if len(pairs) == 0:
        # 짝꿍리스트에 -1 append
        pairs.append(-1)
        
    # 짝꿍리스트를 전부더했을때 0이면
    if sum(pairs) == 0:
        # 짝꿍리스트를 0으로 초기화 
        pairs = [0]
    
    # 짝꿍리스트 내림차순 정렬 
    pairs.sort(reverse = True)
    
    # 짝꿍리스트 문자열로 변환 후 리턴 
    return ''.join(map(str, pairs))