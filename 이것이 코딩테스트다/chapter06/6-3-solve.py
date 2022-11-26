"""
n명의 학생
이름, 성적으로 구분
성적이 낮은 순서대로 이름 출력 
"""

# n 입력
n = int(input())

scores = []
# n번씩 반복하며
for _ in range(n):
    # 학생 이름, 성적을 공백으로 구분하여 입력 
    data = input().split()
    name = data[0]
    score = int(data[1])
    # 성적, 이름을 튜플로 만들어 성적 리스트에 append
    scores.append((score, name))

# 성적순으로 sort
scores.sort()

# 성적리스트를 하나씩 반복하며
for score in scores:
    # 학생이름을 출력(튜플의 두번째 원소, 개행대신 띄어쓰기 )
    print(score[1], end= ' ')