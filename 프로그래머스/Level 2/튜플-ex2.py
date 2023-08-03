def solution(s):
    # {{, }} 를 제거 후 },{으로 나누기
    data = s[2: -2].split("},{")
    # 길이 별로 오름차순 정렬
    data= sorted(data, key = lambda x: len(x))
    answer = []
    for item in data:
        # 각각의 원소 분류
        item = list(map(int, item.split(",")))
        for value in item:
            # 포함되어있지 않으면 삽입
            if value not in answer:
                answer.append(value)
                
    return answer