"""
1부터 45까지 숫자 중 6개 찍어맞추는 복권
일부번호 못알아봄 => 0으로 표기
당첨 가능한 최고순위와 최저순위 
번호가 일치하면 순서상관없이 맞힌거로 인정
lottos: 로또 번호 담긴 배열
win_nums: 당첨번호 담은 배열
당첨가능한 최고 순위, 최저 순위를 배열에 담아 return 

로또 번호와 당첨번호를 읽으면서 현재 당첨을 확인하기
최저순위는 현재 당첨 순위 (현재 맞은 개수) 
최고순위는 0이 다 맞을 경우 (현재 맞은 개수 + 0의 개수)
"""

def solution(lottos, win_nums):
    # 정답 리스트 [최고순위, 최저순위]
    answer = []
    
    # 현재 맞은 개수 now = 0
    now = 0
    # 0의 개수 zeros = 0
    zeros = 0
    # lottos를 하나씩 읽으면서 
    for num in lottos:
        # win_nums에 있으면
        if num in win_nums:
            # 현재 맞은 개수 now 1 증가
            now += 1
        # 0이면
        elif num == 0:
            # 0의 개수 zeros 1증가
            zeros += 1
            
    # 맞은 개수를 인덱스로 가지고 값을 순위로 담는 리스트 wins 
    # 0개~1개일치 6위, 2개 일치 5위... 6개일치 1위. 길이는 7
    wins = [6, 6, 5, 4, 3, 2, 1]
            
    # 최고순위 맞은 개수 best는 현재 맞은 개수 + 0의 개수 
    best = now + zeros
    # 최고순위 맞은 개수가 6보다 크면
    if best > 6:
        # 최구순위 맞은 개수 best는 6
        best = 6
        
    # 최저순위는 현재 맞은 개수 
    # [최고순위, 최저순위] 리턴
    return [wins[best], wins[now]]