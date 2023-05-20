"""
추억점수 = 사진속에 나오는 인물의 그리움 점수를 모두 합산한 값 
각 추억점수를 배열에 담아 리턴하기

photo를 하나씩 탐색하면서 name에 있으면 그에 맞게 추억점수를 매번 더하고 
결과 리스트에 append후 리턴 
"""

def solution(name, yearning, photo):
    # 추억점수들을 원소로 갖는 결과 리스트 
    answer = []
    
    # photo를 하나씩 탐색하면서 원소 people
    for people in photo:
        # 현재 사진에 대한 추억점수 memory 0으로 초기화 
        memory = 0 
        # people를 하나씩 탐색하면서 : 원소 person
        for person in people: 
            # person이 name 안에 있으면
            if person in name: 
                # person을 name에서 인덱스를 찾아 yearning에 인덱스값을 memory에 더함
                memory += yearning[name.index(person)]
        # memory를 answer에 append 
        answer.append(memory)
    
    return answer