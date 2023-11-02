"""
1번부터 n번까지 번호 붙여진 학생. n명의 학생들 키 모두 다름 
두학생끼리 키를 비교한 결과 일부 
a번 학생의 키가 b번 학생의 키보다 작으면 a에서 b로 화살표 그려 표현 
학생들의 키를 비교한 결과 자신의 키가 몇번째인지 알 수 있는 학생 모두 몇명인지 계산
"""
import heapq
import sys
input = sys.stdin.readline 

INF = int(1e9) 

# 학생 수 n, 학생 키 비교횟수 m 입력
n, m = map(int, input().split()) 
# 학생 번호간 키를 그래프형태로 저장. 
graph = [[] for _ in range(n + 1)]
# m번 반복하면서
for _ in range(m): 
    # 두 학생의 키 비교 결과 a, b 주어짐. a인 학생이 번호 b인 학생보다 키가 작음
    a, b = map(int, input().split())
    graph[a].append(b) 
    
# 한 학생에서 다른 학생까지 경로가 확인하는 distance
distance = [[INF] * (n + 1) for _ in range(n + 1)]

# 다익스트라 알고리즘 선언
def dijkstra(distance, start):
    # 자기자신으로 가는 경로는 0으로 초기화
    distance[start][start] = 0 
    # 힙큐 q 빈리스트로 생성
    q = [] 
    # q에 거리, start 삽입
    heapq.heappush(q, (distance[start][start], start))
    
    # q가 빌 때까지 반복 진행
    while q: 
        # 현재 거리 dist, 현재 노드 node는 q에서 pop한 값
        dist, node = heapq.heappop(q)
        
        # distance[start][node]가 dist보다 작으면
        if distance[start][node] < dist: 
            # continue 
            continue
        
        # graph[node]와 연결된 다른 노드들을 확인하면서 : 원소 next
        for next in graph[node]: 
            # next까지 거리 cost는 dist + 1
            cost = dist + 1
            # distance[start][next]보다 cost가 작으면
            if cost < distance[start][next]:
                # distance[start][next]는 cost
                distance[start][next] = cost 
                # q에 (next, cost) 삽입 
                heapq.heappush(q, (cost, next))
                
# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1): 
    # 다익스트라 알고리즘 진행 
    dijkstra(distance, i) 
    
# 자신의 키가 몇번째인지 알 수 있는 학생 students 0 으로 초기화
students = 0 
# 인덱스 i: 1부터 n까지 반복하면서
for i in range(1, n + 1): 
    # 몇번째인지 알수있는 여부 can_find_rank True로 초기화 
    can_find_rank = True 
    # 인덱스 j: 1부터 n까지 반복하면서
    for j in range(1, n + 1): 
        # disntace[i][j] 가 INF보다 같거나 크고 distance[j][i]가 INF보다 같거나 크면 
        if distance[i][j] >= INF and distance[j][i] >= INF: 
            # can_find_rank false로 변경
            can_find_rank = False 
            # continue
            continue 
            
    # can_find_rank가 True이면
    if can_find_rank: 
        # students 1 증가
        students += 1
        
# students 출력 
print(students)