"""
a, b 서로 무게가 다른 볼링공 고름
총 n개 볼링공. 각 볼링공마다 무게가 있음. 
    같은 무게의 공이 여러개 있을 수있으나 서로 다른공으로 간주 
    무게는 1번부터 M까지 자연수 형태 
공의 번호는 1번부터 순서대로 부여
고를 수 있는 볼링공 번호의 조합 경우의수 구하기 
"""
n, m = map(int, input().split())
ball_weights = list(map(int, input().split()))

ball_weights_counts = [0] * (m + 1)
for ball_weight in ball_weights:
    ball_weights_counts[ball_weight] += 1

cases = 0
for i in range(1, m):
    if ball_weights_counts[i] > 0: 
        n -= ball_weights_counts[i] 
        cases += ball_weights_counts[i] * n;

print(cases)