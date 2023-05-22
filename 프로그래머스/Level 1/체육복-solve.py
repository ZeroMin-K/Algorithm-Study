"""
학생들 번호 체격순. 바로 앞번호, 바로 뒷번호 학생에게만 체육복 빌려줌 
체육복이 없으면 수업을 못들어서 적절히 빌려 최대한 많은 학생 수업듣게 함
전체 학생수 n, 체육복 도난 당한 학생 번호 배열 lost, 여벌 체육복 가져온 학생벌호 reserve
체육수업 들을 수 있는 학생 최댓값 리턴

여벌 체육복 가져온 학생이 도난당할 수 있으니 자기자신이 쓰고 빌려주는거 불가 

여벌있는 학생이 한명이고 앞뒤로 모두 가능한데 앞뒤둘다 도난당한 학생이면 어쩌피 한개는 줘야하고
누구를 주든 상관없음 

n+1 길이의 리스트 모두 체육복이 있다는것을 가정해서 원소의 값이 1
lost를 하나씩 탐색하면서 해당 학생들 -1
reserve를 하나씩 탐색하면서 
본인이 0이면 +1, 본인앞자리가 0이면 +1, 본인뒤자리가 0이면 +1 elif로 진행 
체육복가진 학생리스트의 합을 반환 (이때 -1을 해야함 0번인덱스 )

"""

def solution(n, lost, reserve):    
    # 전체 학생리스트 students 길이 n + 1, 모두 1로 초기화
    students = [1] * (n + 1) 
    
    lost.sort()
    reserve.sort()
    
    # lost를 하나씩 탐색하면서 - 원소 lost_person 
    for lost_person in lost: 
        # students[lost_person] 해당 학생들 도난당했으니 -1
        students[lost_person] -= 1
        
    # 여벌있는자기자신이 도난당하고 다시 입은 경우를 제외한 나머지 리스트
    rest_reserve = [] 
    
    # reserve를 하나씩 탐색하면서 : 원소 person 
    for person in reserve: 
        # 여벌있는 본인이 도난 당한 경우 그대로 자기꺼 입기 
        if students[person] == 0:
            students[person] += 1
        else: 
            # 나머지 사람들을 나머지 리스트에 넣음
            rest_reserve.append(person)
            
    # reserve를 하나씩 탐색하면서 - 원소 reserve_person 
    for reserve_person in rest_reserve: 
        # reserve_person이 1보다 크고 reserve_person -1이 0이면
        if reserve_person > 1 and students[reserve_person - 1] == 0:
            # students[reserve_person -1] 1증가
            students[reserve_person - 1] += 1
        # reserve_person이 n보다 작고 reserve_person -1이 0이면
        elif reserve_person < n and students[reserve_person + 1] == 0:
            # students[reserve_person + 1] 1증가
            students[reserve_person + 1] += 1
        
    # 전체 학생 리스트 students의 합 - 1리턴     
    return sum(students) - 1