"""
0번부터 n - 1번까지 n명의 학생 중 3명 선발
참여가능한 학생 중 등수가 높은 3명 선발 
rank: 각 학생들 선발고사 등수 정수 배열 
attendance: 참여 가능 여부 boolean 배열 
return : 선발된 학생 번호 등수 높은 순서대로 a, b, c에서 10000 * a + 100 * b + c 
"""

def solution(rank, attendance):
    result = sorted([(rank[i], i) for i in range(len(rank)) if attendance[i]])
    return 10000 * result[0][1] + 100 * result[1][1] + result[2][1]