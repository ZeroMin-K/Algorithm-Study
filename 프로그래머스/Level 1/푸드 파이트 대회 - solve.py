"""
맨 왼쪽에서 오른쪽으로, 맨 오른쪽에서 왼쪽으로 진행
중앙에 물 배치. 물먼저먹으면 승리
두 선수가 먹는 음식의 종류와 양이 같아야하고 음식을 먹는 순서도 같아야함 
칼로리가 낮은 음식을 먼저 먹을 수 있게 배치

중앙 0을 기점으로 칼로리가 적은순서대로 양쪽이 끝이 같아야함 
food는 칼로리가 적은 순서대로 음식의 양이 담김
food[i] i번 음식의 수 
food[0]은 물의 양 항상 1
칼로리에 맞게 오름차순으로 정렬해서 0붙이고 정렬한걸 다시 내림차순으로 정렬해서 정답 리스트에 붙이기
인덱스 1부터 마지막까지 2로 나눴을때 몫만큼 정답리스트에 붙이고 거꾸로할 리스트에도 붙이고
0을 정답리스트에 붙이고
거꾸로할 리스트를 역순정렬해서 정답리스트에 붙이기 

"""

def solution(food):
    # 정답 리스트
    answer = []
    # 절반 리스트 
    half = [] 
    # 인덱스 i를 1부터 food 길이 -1까지 반복하면서 
    for i in range(1, len(food)):
        # food[i]를 2로 나눴을때 몫만큼 반복하면서    
        for _ in range(food[i] // 2):
            # i를 정답리스트에 append
            answer.append(str(i))
            # i를 절반 리스트에 append
            half.append(str(i))
    # 정답리스트에 0 붙이기
    answer.append('0')
    # 절반 리스트를 역순으로 정렬하여 정답리스트에 append 
    for item in sorted(half, reverse = True):
        answer.append(item)
    return ''.join(answer)