"""
n-튜플: n개의 요소를 가진 튜플 
    1. 중복된 원소 있을 수 있음
    2. 원소에 정해진 순서. 순서가 다르면 서로 다른 튜플
    3. 튜플의 원소 개수 유한
원소의 개수가 n개, 중복되는 원소가 없는 튜플이 주어질때 
    {}를 이용해 표현 가능 
s: 특정 튜플을 표현하는 집합이 담긴 문자열
return : s가 표현하는 튜플 배열 

{{a1}, {a1, a2}, ....{a1,... an}}
{{a1, a2}, ...{a1}}
{{a2, a1}, ...{an, ..a1}}
길이1 : a1 확정
길이2 : {a1, a2}, {a2, a1} => a1이 무엇인지 알고있으니 a2 알 수 있음
...
길이n: {a1,... an}

문자열인 {} 집합들을 리스트로 변환하여 각 길이에 맞게 저장 
길이 1부터 500까지 반복하면서 a1, ...an까지 순차적으로 찾아가기
"""

def solution(s):
    answer = []
    # 집합들을 리스트로 변경해서 길이를 인덱스로 하여 저장하는 리스트 set_list 초기화 : 빈 리스트를 원소로하고 길이가 501
    sets_list = [[] for _ in range(501)]
    # s에서 맨앞 {와 맨뒤 } 제거
    s = s[1:-1]
    # s를 읽으면서 현재 집합에 대한 리스트 set_list 빈리스트로 초기화 
    set_list = [] 
    # 현재 집합이 끝났는지 여부 is_set_end False로 초기화 
    is_set_end = False
    # s를 하나씩 읽으면서 : 원소 letter
    for letter in s: 
        # letter가 {이면 
        if letter == '{':
            # -- 현재 집합 시작 -- 
            # set_list 빈리스트로 초기화
            set_list = [] 
            # is_set_end False로 초기화
            is_set_end = False
        # letter가 }이면  
        elif letter == '}':  
            # -- 현재 집합 끝 --
            # set_list를 join후 ,로 구분한 문자열 리스트로 변경 후 각 문자열을 숫자로 변경한 리스트로 변경
            set_list = [int(num) for num in ''.join(set_list).split(',')]
            # set_list의 길이를 인덱스로 하여 sets_list에 set_list 원소들 삽입 
            for num in set_list:
                sets_list[len(set_list)].append(num)
            # is_set_end True로 전환
            is_set_end = True 
        # letter가 , 인데 현재 집합이 끝인 상태이면
        elif letter == ',' and is_set_end:  
            # 다음 집합으로 넘어감
            continue
        # 나머지의 경우 
        else: 
            # letter를 set_list에 삽입 
            set_list.append(letter)
            
    # 튜플 원소 저장하는 리스트 tuples 
    tuples = [] 
    # tuples에 sets_list[1] 원소를 더함 (튜플에서 a1에 해당)
    tuples.append(sets_list[1][0])
    # 인덱스 i: 2부터 500까지 반복하면서 
    for i in range(2, 501): 
        # 현재 집합은 sets_list[i]
        # sets_list[i]의 길이가 0이면
        if len(sets_list[i]) == 0:
            # 반복 종료
            break
            
        # sets_list[i]에서 sets_list[i - 1]에서 같은것을 제외했을 때 남은 원소가 튜플에서 i번째 원소
        for num in sets_list[i]:
            if num not in sets_list[i - 1]: 
                tuples.append(num)

    return tuples