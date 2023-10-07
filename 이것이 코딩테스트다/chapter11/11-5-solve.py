"""
a, b 두사람이 볼링치는 중 
서로 무게가 다른 볼링공 고름
볼링공은 총 n개, 각 볼링공마다 무게있음
공의 번호는 1번 순서대로 부여
같은 무게의 공이 여러개 있을 수 있으나 서로 다른 공으로 간주
볼링공의 무게는 1부터 m까지 자연수 형태로 존재 
볼랭공을 고르는 경우의 수 구하기 
"""
# 볼링공 개수 n, 공의 최대 무게 m 입력 
n, m = map(int, input().split()) 
# 각 볼링공의 무게 리스트로 입력 
balls = list(map(int, input().split())) 

from itertools import combinations 
answer = 0 
for a, b in list(combinations(balls, 2)): 
    if a != b: 
        answer += 1
print(answer)