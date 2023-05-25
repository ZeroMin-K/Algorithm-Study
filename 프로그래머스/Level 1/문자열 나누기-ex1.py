import sys
sys.setrecursionlimit(10**6)

def solution(s):
    answer = 0
    
    def dfs(strs):
        if strs == "":
            return 
        nonlocal answer
        
        answer += 1
        
        l, r = 0, 0
        x = strs[0]
        for i, v in enumerate(strs):
            if v == x:
                l += 1
            else:
                r += 1
            if l == r:
                dfs(strs[i + 1:])
                break
    dfs(s)
    return answer