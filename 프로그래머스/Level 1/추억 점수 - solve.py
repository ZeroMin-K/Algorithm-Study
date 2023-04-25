"""
그리움 점수를 모두 합산한 값이 해당 사진의 추억점수가 됨
name: 그리워하는 사람의 이름을 담은 문자열 배열
yearning: 각 사람별 그리움 점수를 담은 정수 배열
photo: 각 사진에 이름을 담은 이차원 문자열 배열
return - 추억점수를 배열에 담아 return 

photo를 하나씩 탐색하면서 탐색한 안에서 리스트를 순회하면서 
각 해당하는 점수가 있으면 더하고 더한 값을 리스트에 넣어 리스트를 ㅌ반환 
"""

def solution(name, yearning, photo):
    answer = []
    
    # photo를 하나씩 탐색하면서 - 원소 people 
    for people in photo: 
        # 추억점수 score = 0 
        score = 0 
        # people 원소를 하나씩 탐색하면서 - 원소 person
        for person in people: 
            # person이 name에 있으면
            if person in name: 
                # 인덱스를 찾아서 해당 인덱스로 yearning에서 찾아 더함 
                score += yearning[name.index(person)]
                
        # 최종 score를 answer에 append 함 
        answer.append(score)
            
    return answer