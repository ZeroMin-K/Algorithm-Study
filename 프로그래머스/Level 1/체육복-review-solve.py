"""
학생 번호는 체격순.여벌 체육복이 있으면 빌려줌.
바로 앞번호, 뒷번호 학생에게만 체육복 빌려줄 수 있음
최대한 많은 학생이 체육복 빌림
n: 전체 학생수 
lost: 도난당한 학생번호
reserve: 여벌 가져온 학생 번호
    여벌 체육복 가져온 학생이 체육복 도난당할수있으니
    빌려주는거 불가능하고 오직 자신만 가능
return : 체육수업들을 수있는 학생 최댓값 

도난당하고 여벌있는 자신이 우선순위이므로 lost에 reserve가 같은 번호가 있으면 lost, reserve에서 둘다 제외
앞번호 뒷번호든 무조건 하나만 빌려줄 수 있기 때문에 앞뒤 둘다 없으면 한명만 빌려줄수밖에 없는 구조
reserve보면서 앞뒤로 lost에 해당되는게 있으면 제외시키고 전체 n에서 lost길이 빼기 

"""

def solution(n, lost, reserve):
    # 도난당했지만 여벌이 있는 학생들을 lost, reserve에서 제외
    # 남은 도난당한 학생리스트는 lost를 set로 만들고 reserve를 set로 만들고 빼고 리스트로 만들고 정렬 
    rest_lost = sorted(list(set(lost) - set(reserve)))
    # 남은 여벌있는 학생 리스트는 reserve를 set로 만들고 lost를 set로 만들고 빼고 리스트로 만들고 정렬
    rest_reserve = sorted(list(set(reserve) - set(lost)))
    
    # reserve를 하나씩 탐색하면서 - 원소 reserve_person
    for reserve_person in rest_reserve: 
        # 빌릴 수 있는 이전 번호 reserve_person - 1
        borrow = reserve_person - 1
        # 이전번호가 0보다 크고, 남은 도난 리스트에 있으면
        if borrow > 0 and borrow in rest_lost:
            # 이전번호를 남은 도난 리스트에서 제외 
            rest_lost.remove(borrow)
            continue 
        
        # 빌릴 수 있는 다음 번호 reserve_person + 1
        borrow = reserve_person + 1
        # 혹은 이전번호이 n보다 작거나 같고 남은 도난 리스트에 있으면
        if borrow <= n and borrow in rest_lost: 
            # reserve_person + 1을 남은 도난 리스트에서 제외 
            rest_lost.remove(borrow) 
    
    # 전체n에서 남은 도난 리스트 길이 빼기 
    return n - len(rest_lost)