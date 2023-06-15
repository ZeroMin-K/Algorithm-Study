def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dict_report = {id : [] for id in id_list}
    for i in set(report):
        i = i.split()
        dict_report[i[1]].append(i[0])
        
    for key, value in dict_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1
                
    return answer