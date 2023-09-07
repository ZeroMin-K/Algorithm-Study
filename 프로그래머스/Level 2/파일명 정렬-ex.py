def solution(files):
    splited_files = [] 
    for idx, file in enumerate(files):
        file = file.lower()
        splited_files.append([idx, '', ''])
        number_section = False
        for w in file:
            if w.isdigit():
                number_section = True
                splited_files[-1][2] += w
            else:
                if number_section:
                    break
                splited_files[-1][1] += w
                
        splited_files[-1][2] = int(splited_files[-1][2]) 
    
    splited_files = sorted(splited_files, key = lambda x: (x[1], x[2], x[0]))   
    return [files[file[0]] for file in splited_files]