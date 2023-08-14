def solution(str1, str2):
    str1_list = [str1[i: i + 2].lower() for i in range(len(str1) - 1) if str1[i: i + 2].isalpha()]
    str2_list = [str2[i: i + 2].lower() for i in range(len(str2) - 1) if str2[i: i + 2].isalpha()]
    
    total_list = set(str1_list) | set(str2_list)
    intersection = []
    union = []
    
    if total_list:
        for elem in total_list:
            intersection.extend([elem] * min(str1_list.count(elem), str2_list.count(elem)))
            union.extend([elem] * max(str1_list.count(elem), str2_list.count(elem)))
            
        answer = int(len(intersection) / len(union) * 65536)
    else:
        answer = 65536
    
    
    return answer