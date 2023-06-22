def solution(s):
    stack = []
    
    for i in s:
        # 스택이 비어있는데 닫힌 괄호들어오면 False retur 
        if len(stack) == 0 and i == ')':
            return False
        
        # 스택 맨 위 열린 괄호가 있고 닫힌 괄호가 들어오면 pop
        if i == ')' and stack[-1] == '(':
            stack.pop()
            
        # 열린 괄호가 들어오면 stack에 ㅁppend
        if i == '(':
            stack.append('(')
            
    # 전부 탐색후 스택에 원소가 남아있으면 False return 
    return False if len(stack) != 0 else True