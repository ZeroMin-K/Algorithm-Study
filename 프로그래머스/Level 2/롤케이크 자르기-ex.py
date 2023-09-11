from collections import Counter

def solution(toppings):
    fair_way = 0
    toppingsDict = Counter(toppings)
    toppingsTypes = set()
    
    for topping in toppings: 
        toppingsDict[topping] -= 1
        toppingsTypes.add(topping)
        if toppingsDict[topping] == 0:
            toppingsDict.pop(topping)
        if len(toppingsDict) == len(toppingsTypes):
            fair_way += 1
    
    return fair_way