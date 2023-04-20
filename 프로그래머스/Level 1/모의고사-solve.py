"""
1번 수포자가 찍는 방식: 12345의 연속
2번 수포자가 찍는 방식: 21232425의 연속
3번 수포자가 찍는 방식 3311224455의 연속 
answers의 길이만큼 각 수포자 리스트의 길이를 늘려서 
answers하나씩 확인하며 맞은 횟수 카운트하고 가장 큰 값 찾기 
가장 높은 점수받은 사람이 여럿이면 오름차순 정렬 
"""

def solution(answers):
    answer = []
    # answers의 길이 
    length = len(answers)
    # 1번 수포자가 찍는 방식의 리스트 - answers 길이 곱으로 만듬
    first = [1, 2, 3, 4, 5] * length 
    # 2번 수포자가 찍는 방식의 리스트 
    second = [2, 1, 2, 3, 2, 4, 2, 5] * length 
    # 3번 수포자가 찍는 방식의 리스트
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * length 
    
    # 1, 2,3번 수포자의 정답 개수 리스트 (길이4 - 인덱스0제외)
    corrects = [0, 0, 0, 0]
    
    # 인덱스 i - 0부터 answers 길이 - 1 만큼 반복하면서 
    for i in range(length):
        # answers[i]와 1번수포자 i번째 답이 맞으면
        if answers[i] == first[i]:
            # 1번 수포자 정답 증가
            corrects[1] += 1
        # answers[i] 와 2번수포자 i번째 답이 맞으면
        if answers[i] == second[i]:
            # 2번 수포자 정답 증가
            corrects[2] += 1
        # answers[i] 와 3번 수포자 i번째 답이 맞으면
        if answers[i] == third[i]:
            # 3번 수포자 정답 증가 
            corrects[3] += 1
    
    # 정답 개수 리스트에서 max값 찾음
    max_answer = max(corrects)
    # 인덱스 i - 1부터 3까지 반복하면서
    for i in range(1, 4):
        # 정답개수리스트 i(i번째 수포자)가 max와 같으면
        if corrects[i] == max_answer:
            #정답 리스트에 i append 
            answer.append(i)
            
    return answer