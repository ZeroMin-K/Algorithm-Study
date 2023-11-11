"""
n개의 전구. 맨왼쪽에 있는 전구가 첫번째
전구 상태 두가지. 1: 켜짐, 0: 꺼짐
전구제어명령어 4개
1. i번째 전구상태 x로 변경
2. l번째부터 r번째까지 전구 상태 변경
3. l번째부터 r번째까지 전구 끔
4. l번째부터 r번째까지 전구 킴 

명령어 다 수행한 결과 전구는 어떤 상태인지 
"""
# 전구 개수 n, 명령어 개수 m 입력
n, m = map(int, input().split())
# n개의 전구가 현태 어떤상태인지 s 주어짐
bulbs = list(map(int, input().split()) )
# m번 반복하면서 
for _ in range(m): 
    # a, b, c 입력 : a는 a번째 명령어. b,c는 a가 1인 경우 i,x a가 2,3,4 중 하나면 l, r
    a, b, c = map(int, input().split())
    
    if a == 1:
        bulbs[b - 1] = c
    elif a == 2:
        for i in range(b - 1, c):
            if bulbs[i] == 1:
                bulbs[i] = 0
            else: bulbs[i] = 1
    elif a == 3:
        for i in range(b - 1, c):
            bulbs[i] = 0
    elif a == 4:
        for i in range(b - 1, c):
            bulbs[i] = 1
    
for bulb in bulbs:
    print(bulb, end = ' ')