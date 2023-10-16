def solution(ineq, eq, n, m):
    answer = int(n > m) if ineq == '>' else int(n < m)
    return answer if eq == '!' else int(answer or n == m)