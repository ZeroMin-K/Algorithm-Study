"""
n명의 학생 키순서대로 줄세움 
두 학생의 키를 비교
일부 학생들의 키를 비교한 결과가 주어졌을때 줄세우는 프로그램
위상 정렬 이용 
"""

import sys
input = sys.stdin.readline

# 학생 수 n, 키 비교횟수 m 입력
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegrees = [0] * (n + 1) 
# m번 반복하면서
for _ in range(m): 
    # a, b 입력. a가 학생 b의 앞에 서야한다
    a, b = map(int, input().split()) 
    graph[a].append(b)
    indegrees[b] += 1
    
from collections import deque
q = deque()
students = [] 

for i in range(1, n + 1):
    if indegrees[i] == 0:
        q.append(i) 

while q:
    student = q.popleft()
    students.append(student)
    
    for next in graph[student]:
        indegrees[next] -= 1
        
        if indegrees[next] == 0:
            q.append(next)

# 줄 세운 결과 (답 여러가지있을 수 있음 )
for student in students:
    print(student, end = ' ')