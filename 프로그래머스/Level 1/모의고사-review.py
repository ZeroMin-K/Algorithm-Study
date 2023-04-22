"""
인덱스를 나머지 연산을 통해서 구해서 풀이 진행 


"""

def solution(answers):
    # 각 수포자들이 찍는 방식에 대한 리스트  picks 
    picks = [
        [], 
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
        
    # 수포자가 맞힌 문제 개수 리스트 길이4 , 0으로초기화 totals 
    totals = [0] * 4
    
    # 인덱스 i를 0부터 answers의 길이-1까지 반복하면서
    for i in range(len(answers)):
        # picks 리스트 인덱스 j - 1부터 반복하면서 3까지 진행
        for j in range(1, 4):
            # picks[j] - 1, 2, 3은 각 수포자 리스트 
            # answers[i]와 picks[j][i % len(picks[j])] 가 같으면
            if answers[i] == picks[j][i % len(picks[j])]:
                # totals[j] 에 1 추가 
                totals[j] += 1
    
    # 수포자가 맞힌 문제 리스트최대값
    # 수포자 문제 개수 리스트 하나씩 확인하며 인덱스 i는 1부터 3까지 
        # 문제 리스트 최대값과 같으면 
            # 결과리스트에 i를 append
    answer = [i for i in range(1, 4) if totals[i] == max(totals)]
    
    
    return answer