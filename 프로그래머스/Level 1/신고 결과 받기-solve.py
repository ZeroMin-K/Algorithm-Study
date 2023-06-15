"""
각 유저는 한번에 한명의 유저 신고
    - 신고 횟수 제한 없음. 서로 다른 유저 계속 신고 가능
    - 한 유저 여러번 신고 가능하지만 동일한 유저에 대한 신고 횟수는 1회 처리 
k번 이상 신고된 유저는 게시판 이용 정지. 해당 유저를 신고한 모든 유저에게 정지사실을 메일로 발송
    - 유저가 신고한 모든 내용 취합. 마지막에 한꺼번에 게시판 이용정지 시키면서 정지 메일 발송

id_list: 이용자 id가 담긴 문자열 배열
report: 각 이용자가 신고한 이용자 id 정보가 담긴 문자열 배열
    - "이용자id 신고한id" 형태의 문자열 원소. 공백하나로 구분. 
k: 정지 기준 신고횟수 
return : 각 유저별로 처리결과 메일을 받은 횟수 배열 

각 유저를 키로 정지 메일 발송수를 값으로 갖는 딕셔너리와
키를 신고당한 유저로 신고한 유저 리스트를 값으로 갖는 딕셔너리를 이용
report를 하나씩 탐색하여 신고당한 유저들의 신고한 유저리스트를 만듬
동일한 유저에 대한 신고횟수는 1회로 처리되기때문에 
report 전부 탐색 후 신고한 유저리스트를 set로 만들고 다시 list로 만들어줌
신고한 유저리스트가 k번이 넘으면 유저들의 신고한 유저리스트를 하나씩 탐색하면서 정지메일 발송수 증가 
id_list의 순서에 맞게 유저들의 정지 메일 발송수를 리스트로 만들어 리턴 

"""

def solution(id_list, reports, k):
    # id_list를 읽으며 id_list의 원소 유저id를 키로 값은 0으로 하는 각 유저별로 정지메일 받은수를 저장하는 딕셔너리 mails
    mails = {user_id : 0 for user_id in id_list}
    # id_list를 읽으며 id_list의 원소 유저id를 키로 값은 빈 리스트로 하는 해당 유저를 신고한 유저 리스트를 저장하는 딕셔너리 reports_dict
    reports_dict = {user_id : [] for user_id in id_list}
    
    # reports를 하나씩 탐색하면서 - 원소 report (유저 신고한id)
    for report in reports: 
        # report를 공백 기준으로 유저id  user,  신고한 유저id reported_user로 나눔
        user, reported_user = report.split(' ')
        # reported_user를 키로 reports_dict값에 user를 append
        reports_dict[reported_user].append(user)
        
    # report_dict 를 하나씩 탐색하면서 신고를 한 유저리스트를 set로 만들고 다시 list로 변경 
    reports_dict = {user_id : list(set(reported_list)) for user_id, reported_list in reports_dict.items()}
    
    # reports_dict 값들을 하나씩 탐색하면서 -값 report_users 리스트 
    for report_users in reports_dict.values():
        # report_users의 길이가 k 이상이면 
        if len(report_users) >= k:
            # report_users를 하나씩 탐색하면서 - 원소 report_user
            for report_user in report_users:
                # mails에서 report_user를 키로 값을 1씩 증가
                mails[report_user] += 1
                
    # id_list를 하나씩 탐색하면서 원소 user를 키로 mails에서 값을 원소로 갖는 리스트 생성하여 반환
    return [mails[user_id] for user_id in id_list]