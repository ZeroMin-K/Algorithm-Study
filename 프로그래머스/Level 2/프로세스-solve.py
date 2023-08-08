"""
운영체제가 규칙에 따라 프로세스 관리시 특정 프로세스가 몇번째로 실행되는지 알아내기
1. 실행 대기 큐에서 대기중인 프로세스 하나꺼냄
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣음
3. 만약 그런 프로세스가 없다면 방금꺼낸 프로세스 실행
    3-1. 한번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료 
priorities: 현재 실행 대기 큐에 있는 프로세스 중요도가 순서대로 담긴 배열
    - 1이상 9이하 정수 원소
    - 숫자가 클수록 우선순위가 높음 
location: 몇번째로 실행되는지 알고싶은 프로세스 위치
    - 0이상 (대기큐 프로세스 수 - 1) 이하의 값
    - 가장 앞에 있으면 0, 두번째 1 => 결국 인덱스 
return : 해당 프로세스가 몇번째에 실행되는지

우선순위가 가장 높은 프로세스부터 꺼낸다 => 최대 힙을 이용 
=> 같은 우선순위여도 순서가 있음. 우선순위와 인덱스를 기준으로 우선순위는 내림차순, 인덱스는 오름차순으로 정렬 
"""

def solution(priorities, location):
    
    # deque import 
    from collections import deque
    # 프로세스 대기 큐 q deque로 생성
    q = deque()
    # priorities를 enumerate로 하나씩 탐색하면서: 인덱스 idx, 원소 priority
    for idx, priority in enumerate(priorities):
        # q에 (priority, idx) 삽입
        q.append((priority, idx))
    # priorities를 내림차순 정렬 후 deque로 변경
    priorities = deque(sorted(priorities, reverse = True))

    # 현재 실행순서 execution_order 1로 초기화 
    execution_order = 1
    # q가 빌때까지 반복하면서 
    while q:
        # q에서 popleft함 우선순위 priority, 인덱스 idx
        priority, idx = q.popleft()
        # priority와 priorities[0]과 같으면 
        if priority == priorities[0]:
            # idx와 location이 같으면
            if idx == location:
                # 반복 봉료
                break
            # 다르면
            else:
                # execution_order 1증가 
                execution_order += 1
                # priorities popleft
                priorities.popleft()
        # 다르면 (나머지 경우)
        else:
            # (priority, idx)를 q에 삽입
            q.append((priority, idx))
    
    # execution_order 리턴
    return execution_order