"""
최소한 객실만을 사용하여 예약 손님 받기
한번 사용한 객실은 퇴실시간 기준 10분간 청소후 다른 손님 사용가능
book_time: 예약시간이 문자열 형태로 담긴 2차월 배열
    - [시작 시각, 종료 시각] ["HH:MM", "HH:MM"]
    - 24시간 표기법
return : 필요한 최소 객실 수 

24시간을 분단위로 하여 시작 시간 ~ 종료시각 + 10분까지 겹치는 시간들 중 최댓값 찾기
종료시각, 시작시간이 겹치는 경우 있음 => 종료시각 + 9로 따지기
최소 객실수가 필요하지만 겹치는 시간이 최대인 곳만큼 객실수 필요.
"""

# 시간을 받아서 :을 구분하여 분단위로 변경
def convert_time(time):
    hour, min = map(int, time.split(':'))
    return hour * 60 + min 

def solution(book_time):
    # 00:00 ~ 23:59분을 분단위로 하여 분을 인덱스로 원소는 0인 24 * 60 크기의 리스트 times 생성
    times_len = 24 * 60 
    times = [0] * (times_len)
    # book_time을 하나씩 탐색하면서 : 원소 start_time, end_time
    for start_time, end_time in book_time: 
        # convert_time을 호출하여 start_time을 분 단위로 변경
        start_time = convert_time(start_time)
        # convert_time을 호출하여 end_time을 분단위로 변경
        end_time = convert_time(end_time)
        end_time = times_len if (end_time + 9) >= times_len else end_time + 10 
        
        # 인덱스 i: start_time부터 end_time까지 반복하면서
        for i in range(start_time, end_time): 
            # times[i] 1씩 증가 
            times[i] += 1
            
    # times중 최댓값 리턴 
    return max(times)