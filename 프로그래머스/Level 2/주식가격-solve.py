"""
prices: 초단위로 기록된 주식 가격이 담긴 배열
    - 원소 1 이상 10,000 이하 자연수
    - 길이 2 이상 100,000이하 
return : 가격이 떨어지지 않은 기간 (초) 
"""
def solution(prices):
    # 가격이 떨어지지 않은 기간 담는 리스트 periods 원소는 [0] prices길이로 초기화 
    periods = [0] * len(prices) 
    # 초, 주식 가격을 담는 리스트 records (스택으로 사용) 
    records = [] 
    
    # prices를 enumerate를 이용해 탐색 : 원소 idx, price
    for idx, price in enumerate(prices):
        # records가 비어있지 않고 price가 records[-1][1]보다 작으면 
        while records and price < records[-1][1]: 
            # record를 records에서 pop
            record = records.pop() 
            # periods[record[0] - 1]은 (idx + 1) - record[0]
            periods[record[0] - 1] = (idx + 1) - record[0]
            
        # (idx + 1, price)를 records에 삽입 
        records.append((idx + 1, price))
            
    # 마지막 시점 last는 prices길이 
    last = len(prices) 
    # records가 빌 때까지 반복하면서
    while records: 
        # record는 records에서 pop한 값
        record = records.pop()
        # periods[record[0] - 1]의 값은 last - record[0] 
        periods[record[0] - 1] = last - record[0] 
    
    # periods 리턴
    return periods