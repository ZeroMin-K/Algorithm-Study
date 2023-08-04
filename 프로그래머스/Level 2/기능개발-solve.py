"""
기능개선 작업 수행중. 진도가 100%일때 서비스에 기능 반영 가능
각 기능의 개발속도는 모두 다름
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고 뒤에 기능은 앞에 있는 기능이 배포될때 함께 배포 

progresses: 먼저 배포되어야하는 순서대로 작업의 진도가 적힌 정수 배열
speeds: 각 작업의 개발속도가 적힌 정수 배열 
return : 각 배포마다 몇개의 기능이 배포되는지 return 
배포는 하루에 한번. 하루의 끝에 이루어짐  

"""

def solution(progresses, speeds):
    # 배포된 기능 개수들을 저장하는 리스트 releases 빈리스트로 초기화 
    releases = []
    
    # 각 기능마다 완료되는 작업 완료되는 날짜를 저장하는 리스트 completes 리스트컴프리헨션으로 구현
    # - progresses와 speeds를 zip을 이용하여 하나씩 탐색하면서 원소 progress, speed
    # - 100에서 progress를 뺀 후 speed로 나눈 몫이 작업일자. 나머지가 있으면 + 1
    completes = [(100 - progress) // speed if (100 - progress) % speed == 0 else (100 - progress) // speed + 1 for progress, speed in zip(progresses, speeds)]
    
    # deque import
    from collections import deque
    # completes를 deque로 변환
    completes = deque(completes)
    
    # 배포의 기준 날짜 release_day completes에서 popleft했을때 날짜 (첫 기능 배포날짜)
    release_day = completes.popleft()
    # 현재 배포할 기능 개수 release_num = 1 (첫 기능)
    release_num = 1
    # completes가 빌 때까지 반복하면서
    while completes:
        # 다음 작업완료된 기능 complete는 completes에서 popleft
        complete = completes.popleft()
        # complete가 release_day보다 같거나 작으면
        if complete <= release_day:
            # release_num 1 증가 (현재 기능이 일찍끝나서 같이 배포 가능)
            release_num += 1
        # complete가 relase보다 크면 (나머지 경우)
        else:
            # release_num을 releases에 삽입
            releases.append(release_num)
            # release_day는 complete로 초기화 
            release_day = complete
            # release_num 1로 초기화
            release_num = 1
    
    # 마지막 기능들 배포 
    releases.append(release_num)
            
    # releases 리턴  
    return releases