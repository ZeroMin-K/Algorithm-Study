"""
30명의 학생. 1번부터 30번까지 출석번호 있음
과제 28명 제출 
제출 안한 학생 2명의 출석번호 구함
"""
students = 30 
submited = [False] * (students + 1) 

submits = 28 
for _ in range(submits): 
    student = int(input())
    submited[student] = True 

for i in range(1, students + 1):
    if not submited[i]:
        print(i) 