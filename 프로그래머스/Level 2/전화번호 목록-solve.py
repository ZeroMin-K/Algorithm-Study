"""
전화번호부에 적힌 전화번호 중 한 번호가 다른 번호의 접두어인경우 확인 
phone_book: 전화번호부에 적힌 전화번호 담은 배열
return : 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false, 그렇지 않으면 true 
"""
def solution(phone_book):
    answer = True
    
    # 전화번호 접두어를 키로 하여 전화번호 리스트를 값으로 갖는 딕셔너리 phone_book_dict 생성 
    phone_book_dict = dict() 
    # phone_book 하나씩 탐색하면서 : 원소 phone
    for phone in phone_book:
        # 인덱스 i: 1부터 phone의 길이만큼 반복하면서 
        for i in range(1, len(phone) + 1):
            # phone을 i - 1까지 슬라이싱했을때 phone_book_dict 안에 키가 있으면 
            if phone[:i] in phone_book_dict:
                # phone[:i]를 키로하여 phone_book_dict 값에 phone 삽입 
                phone_book_dict[phone[:i]].append(phone) 
            # 키가 없으면 
            else:
                # phone을 원소로 하는 리스트를 값으로 설정 
                phone_book_dict[phone[:i]] = [phone]
                
    # 어떤 번호가 다른 번호의 접두어인 경우 answer False로 초기화 
    answer = True
    # phone_book 하나씩 탐색하면서 : 원소 phone
    for phone in phone_book:
        # phone을 키로 했을 때 phone_book_dict 값인 리스트의 길이가 2 이상이면 
        if len(phone_book_dict[phone]) >= 2:
            # answer False로 초기화 
            answer = False 
    
    return answer