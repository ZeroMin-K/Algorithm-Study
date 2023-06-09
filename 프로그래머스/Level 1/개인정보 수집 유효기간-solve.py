"""
개인정보 n개: 1~n번으루 분류
    - 종류는 여러가지, 유효기간 정해짐
수집된 개인정보는 유효기간전까지만 보관 가능. 유효기간 지나면 파기 
today: 오늘 날짜 문자열
    -"YYYY.MM.DD"
terms: 약관 유효기간 담은 1차원 문자열 배열
    - "약관종류 유효기간" 공백하나로 구분 
    - 약관종류 A ~ Z. 중복되지 않음
    - 유효기간. 달수 1 ~ 100 
privacies: 개인정보담은 1차원 문자열 배열
    - "수집일자날짜 약관종류" 
    - 날짜: "YYYY.MM.DD" today 이전날짜
    - 약관종류는 항상 terms에 있는 종류
return : 파기해야할 개인정보 번호를 담은 1차원 정수 배열. 오름차순 

privacies를 하나씩 탐색하면서 terms에 맞게 파기날짜를 확인한뒤 today보다 작거나 같으면 파기하는 리스트에 번호를 넣음
파기 번호 리스트를 오름차순 정렬 후 리턴 

"""

def solution(today, terms, privacies):
    # 파기해야할 개인정보 번호를 담는 리스트
    answer = []
    
    # 오늘 날짜를 오늘 연, 월, 일로 나눔
    today_year, today_month, today_day = map(int, today.split('.'))
    
    # 약관종류를 키를 종류, 값을 유효기간 달수로 하는 딕셔너리 생성. 
    terms_dict = {}
    # 약관종류 terms를 하나씩 탐색하면서 - 원소 term 
    for term in terms: 
        # term을 공백 기준으로 종류와 개월수를 분리
        term_type, expire_date = term.split(' ')
        # 야관 종류를 키로 하고 개월 수를 정수로 변환한뒤 값으로 한뒤 딕셔너리에 삽입
        terms_dict[term_type] = int(expire_date)
    
    # 개인정보 담은 privacies를 하나씩 탐색하면서 - 원소 privacy 인덱스 i
    for i, privacy in enumerate(privacies):
        # 현재 개인정보 privacy를 공백을 기준으로 하여 수집 날짜, 약관 종류로 나눔
        date, term = privacy.split(' ')
        # 다시 수집 날짜를 수집 연, 월, 일로 나눔 
        year, month, day = map(int, date.split('.'))
        
        # 약관 종류를 키로하여 유효기간 달수를 찾아서 수집날짜 월에 더해서 파기날짜를 계산 
        month += terms_dict[term]
        # 월이 12월이 넘는동안
        while month > 12: 
            # 유효기간에 1을 더해줌
            year += 1
            # 월에 12를 뺌 
            month -= 12       
        
        # 파기날짜의 연이 오늘 날짜 연보다 작으면
        if year < today_year: 
            # 현재 개인정보 번호 i + 1을 파기 리스트에 append
            answer.append(i + 1) 
        # 파기날짜의 연이 오늘 날짜 연과 같으면
        elif year == today_year:
            # 파기 날짜의 월이 오늘 날짜 월보다 작으면
            if month < today_month: 
                # 현재 개인정보 번호 i + 1을 파기 리스트에 append
                answer.append(i + 1) 
            # 파기 날짜의 월이 오늘 날짜 월과 같고, 파기 날짜 일이 오늘 날짜의 일과 같거나 작으면 
            elif month == today_month and day <= today_day: 
                # 현재 개인 정보 번호 i + 1을 파기 리스트에 append
                answer.append(i + 1)
    
    # 파기해야할 개인정보 리스트를 정렬해서 리턴 
    return sorted(answer)