import sys
input = sys.stdin.readline

# 학생 수 n 입력
n = int(input())

results = []

# n번 반복하며
for _ in range(n):
    # 이름, 국어, 영어, 수학 점수 공백으로 구분하여 입력 
    name, kor, eng, math_score = input().split()
    results.append((name, int(kor), int(eng), int(math_score)))

# 국어 내림차순, 영어오름차순, 수학내림차순, 이름 사전순증가로 정렬 
results.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 정렬후 한명씩 이름 출력 
for student in results:
    print(student[0])