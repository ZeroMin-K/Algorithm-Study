"""
수확한 귤중 k개 골라 상자 하나에 담아 판매
귤을 크기별로 분류했을때 서로 다른 종류의수를 최소화 
k: 한 상자에 담으려는 귤의 개수 k
tangerine: 귤의 크기 담은 배열
return : 귤 k고를때 크기가 서로 다른 종류 수의 최솟값 

각 크기에 따라 귤의 개수를 세서 가장 많은 개수 귤들을 차례대로 전부 넣으면서 k개가 될때까지 종류 수 세기 
"""

def solution(k, tangerines):
    # 인덱스를 귤의 크기 종류로 하고 값을 해당 크기의 개수로 하는 tangerines_nums 리스트 
    # - 값은 0, 길이는 tagerines의 최댓값 + 1로 초기화
    tangerines_nums = [0] * (max(tangerines) + 1)
    
    # tangerines를 하나씩 탐색하며 - 원소 tangerine
    for tangerine in tangerines: 
        # tangerines_nums[tangerine] 1 증가 
        tangerines_nums[tangerine] += 1
    
    # tangerines_nums 내림차순 정렬 
    tangerines_nums.sort(reverse = True) 

    # 현재 상자에 담는 귤 수 total 0으로 초기화 
    total = 0
    # 크기 종류 최솟값 min_types 0으로 초기화 
    min_types = 0
    # tangerines_nums 하나씩 탐색하면서 - 원소 tangerine
    for tangerine in tangerines_nums: 
        # total에 tangerine을 더함
        total += tangerine
        # min_types 1 증가 
        min_types += 1
        # total이 k보다 같거나 크면 
        if total >= k: 
            # break
            break
    
    return min_types