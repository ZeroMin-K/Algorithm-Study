"""
n명 이름, 국어, 영어, 수학 점수 
학생성적 정렬
1. 국어 점수 감소
2. 영어점수 증가
3. 수학점수 감소
4. 이름 사전순 증가 
"""
import sys
input = sys.stdin.readline

# 반 학생수 n입력
n = int(input())
# 학생들 점수 넣는 리스트 students
students = [] 
# n번 반복하면서
for _ in range(n): 
    # 이름, 국어, 영어, 수학 점수 공백구분 입력
    name, kor, eng, mat = input().split()
    students.append((name, int(kor), int(eng), int(mat)))

students.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

# 정렬 후 n개줄을 거쳐 학생이름 출력 
for student in students:
    print(student[0])