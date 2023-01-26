"""
원래 이용료 price   
놀이기구 n번째 이용시 원래 이용료의 n배 받음
count번 타게되면 현재 자신이 가지고 있는 금액에서 얼마가 모자르는지 return 
각 배수에 대한 원소를 리스트컴프리헨션을 사용하여 리스트 생성. 
생성한 리스트의 합을 구해서 확인 
money와 차이를 구해서 리턴 
"""
def solution(price, money, count):    
    prices_sum = sum([price * i for i in range(1, count + 1)])

    return prices_sum - money if money < prices_sum else 0