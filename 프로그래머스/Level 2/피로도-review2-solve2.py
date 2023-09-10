def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(now_fatigue, completed_dungeons):
        nonlocal max_completed_dungeons_num
        
        for i in range(len(dungeons)):
            if not visited[i] and now_fatigue >= dungeons[i][0]:
                visited[i] = True
                dfs(now_fatigue - dungeons[i][1], completed_dungeons + 1)
                visited[i] = False
                
        max_completed_dungeons_num = max(max_completed_dungeons_num, 
																					completed_dungeons) 
        
    max_completed_dungeons_num = 0 
    
    dfs(k, 0)
    
    return max_completed_dungeons_num