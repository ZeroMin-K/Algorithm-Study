"""
절대값이 10^c 형태 정수 적힌 버튼
현재 층수에 버튼에 적혀있는값을 더한 층으로 이동 
엘리베이터가 위치해있는 층가 버튼의 값을 더한 결과가 0보다 작으면 움직이지 않음
0층이 가장 아래층. 현재 민수가 있는 층
버튼 한번당 마법의 돌 한개 사용 

최소한 버튼을 눌러서 이동
어떤 층에서 0층으로 내려가는데 필요한 마법의 돌 최소개수 
storey: 엘리베이터 위치. 
return : 0층으로 가기 위해 필요한 마법의 돌 최솟값 
"""
def solution(storey):
    stones = 0
    while not (storey == 0): 
        while storey % 10 == 0:
            storey //= 10 
        
        last_digit = storey % 10 
        
        if last_digit > 5:
            storey += 10 - last_digit
            stones += 10 - last_digit
        elif last_digit < 5:
            storey -= last_digit
            stones += last_digit 
        else:
            last_from_second_digit = (storey % 100 - last_digit) // 10
            if last_from_second_digit >= 5:
                storey += 5
            else:
                storey -= 5
            stones += 5
            
    return stones