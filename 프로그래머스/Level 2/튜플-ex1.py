def solution(s):
    answer = []
    
    s = s.lstrip('{').rstrip('}').split('},{')
    
    new_s = [] 
    for i in s:
        new_s.append(i.split(','))
        
    new_s.sort(key = len)
    
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
                
    return answer