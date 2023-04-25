"""
n명을 조건으로 학생 설정 정렬 
1. 국어 점수 감소
2. 영어 점수 증가
3. 수학 점수 감소
4. 이름이 사전 순 

"""
import sys
input = sys.stdin.readline

# 학생 수 n명 입력
n = int(input())

# 성적 리스트 
students = [] 

# n번 반복하면서
for _ in range(n): 
    # 이름, 국어, 영어, 수학 점수 공백 구분해 입력 
    name, kor, eng, maths = input().split()
    students.append((name, int(kor), int(eng), int(maths)))

# 정렬 진행 
students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 이름 출력 
for student in students:
    print(student[0])