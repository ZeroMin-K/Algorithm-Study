"""
매 게임 시작시 건물 짓는 순서 주어짐
모든 건물은 각 건설을 시작하여 완성될때까지 딜레이 존재 
특정 건물을 가장 빨리 지을때까지 걸리는 최소 시간 출력 
건물번호 1번부터 N번까지 존재
동시에 건물 시작 진행 가능 

위상 정렬을 이용하여 계산
이때 동시에 진행하는 건물 중 최대 건설시간을 찾아서 계산 

"""
# 빠른 입력 설정 
import sys
input = sys.stdin.readline 
# deque import 
from collections import deque 

# 테스트케이스 개수 t 입력
t = int(input()) 
# t번 반복하면서 
for _ in range(t): 
    # 건물의 개수 n, 건물순서 규칙 k 입력
    n, k = map(int, input().split())
    # 각 건물 건설에 걸리는 시간 construction_times 리스트로 입력
    construction_times = list(map(int, input().split())) 
    
    # 각 건물들 연결 정보를 알려주는 graph. 원소를 리스트로 길이는 n
    graph = [[] for _ in range(n)]
    # 진입차수 기록하는 indegrees 원소는 0, 길이는 n
    indegrees = [0] * n 
    # k번 반복하면서
    for _ in range(k): 
        # x, y입력. 건물 x를 지은다음 y를 짓는 것이 가능
        x, y = map(int, input().split())
        # graph[x-1]에 y - 1삽입
        graph[x - 1].append(y - 1)
        # indegrees[y - 1] 1 증가
        indegrees[y - 1] += 1 
            
    # 최종적으로 건설해야할 건물 번호 W
    w = int(input())
    w -= 1
    
    # 큐 q deque로 생성
    q = deque() 
    
    # 각 건물까지 짓는데 필요한 시간 dp테이블
    building_times = [0] * (n)
    
    # 인덱스 i: 0부터 n - 1까지 반복하면서
    for i in range(n): 
        # indegree[i]가 0일 때
        if indegrees[i] == 0: 
            # q에 (i) 삽입 
            q.append(i) 
            building_times[i] = construction_times[i]
            
    # q가 빌 때까지 반복 진행
    while q: 
        # 현재 건물 building 는 q에서 pop한 값 
        building = q.popleft() 
        
        # graph[building]와 연결된 다른 노드들을 탐색하면서 : next
        for next in graph[building]: 
            # indegrees[next] 1감소
            indegrees[next] -= 1
            
            building_times[next] = max(building_times[next], building_times[building] + construction_times[next])
            
            # indegrees[next]가 0이면  
            if indegrees[next] == 0: 
                # 큐에 (next, now_stage + 1) 삽입 
                q.append(next)
    
    # 건물 w를 건설완료하는데 최소시간 building_time 출력 
    print(building_times[w])