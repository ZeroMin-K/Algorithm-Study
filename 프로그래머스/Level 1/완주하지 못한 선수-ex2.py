def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    
    for person in participant:
        dic[hash(person)] = person
        temp += int(hash(person))
        
    for person in completion:
        temp -= hash(person)
    
    answer = dic[temp]
    
    return answer