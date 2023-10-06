"""
모든 전공과목을 듣고 졸업
선수과목이 있어 모든 과목을 먼저 이수해야만 해당 과목 이수가능
선수과목 조건을 지킬 경우 전공과목을 언제 이수할 수 있는지 궁금
조건을 간호화하여 계산
1. 한학기에 들을 수 있는 과목 수 제한없음
2. 모든 과목은 매학기 항상 개설됨

모든 과목에 대해 각 과목을 이수하려면 최소 몇학기 걸리는지 계산 
"""

# 빠른 입력 변경
import sys 
input = sys.stdin.readline 
# 과목 수 n, 선수 조건 수 m 입력 
n, m = map(int, input().split()) 
# 각 과목의 선수조건을 저장하는 그래프 graph 원소는 빈리스트 길이는 n + 1로 초기화 
graph = [[] for _ in range(n + 1)] 
# 진입차수를 저장하는 테이블 indegress 값은 0 길이는 n + 1로 초기화 
indegrees = [0] * (n + 1) 
# m번 반복하면서 
for _ in range(m): 
    # a, b 입력
    a, b = map(int, input().split())
    # graph[a]에 b 삽입
    graph[a].append(b) 
    # indegrees[b] 1 증가 
    indegrees[b] +=1 
    
# 각 과목을 이수하기 위한 최소 학기수 completes 값을 1로 길이는 n + 1로 초기화 
completes = [1] * (n + 1)

# deque import 
from collections import deque 
# 큐 q deque로 생성 
q = deque() 
# 인덱스 i: 1부터 n까지 반복하면서 
for i in range(1, n + 1): 
    # indegrees[i]가 0이면
    if indegrees[i] == 0:  
        # q에 i 삽입 
        q.append(i) 
        
# q가 빌 때까지 반복
while q: 
    # 현재 학기 now는 q에서 popleft한 것
    now = q.popleft() 
    # graph[now]를 하나씩 반복하면서 : 원소 next 
    for next in graph[now]: 
        # indegrees[next] 1 감소 
        indegrees[next] -= 1
        # indegrees[next]가 0이면 
        if indegrees[next] == 0: 
            # q에 next 삽입 
            q.append(next) 
            # completes[next]의 값은 completes[now] + 1 
            completes[next] = completes[now] + 1
        
# 인덱스 i: 1부터 n까지 반복하면서 
for i in range(1, n + 1): 
    # completes[i] 출력. end는 공백
    print(completes[i], end = ' ')