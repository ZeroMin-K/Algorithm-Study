"""
주차장의 요금표와 차량이 들어오고 입차, 출차 기록이 주어짐. 차량별로 주차 요금 계산 
어떤 차량이 입차된 후에 출차된 내역이 없다면 23: 59에 출차된것으로 간주 
00:00 ~ 23:59 까지 입/출차 내역을 바탕으로 차량별 누적 주차 시간을 계산하여 요금 일괄로 정산 
누적 주차 시간이 기본 시간 이하라면 기본 요금 청구
누적 주차 시간이 기본시간 초과하면 기본요금에 더해 초과한 시간에 대해 단위시간마다 단위요금 청구
    - 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림
    - ⌈a⌉ : a보다 작지 않는 최소의 정수. 올림 의미 
fees: 주차 요금을 나타내는 정수 배열. 길이 4
    - [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위요금(원)]
records: 자동차의 입/출차 내역 문자열 배열   
    - "시각 차량번호 내역" 형식의 문자열. 공백으로 구분
    - 시각:  HH:MM 형식 길이 
    - 차량번호: 0~9로 구성된 길이4문자열
    - 내역 : IN or OUT 
    - 시각 기준 오름차순
    - 잘못된 입력 주어지지 않음
        - 같은 시각, 같은 차량번호 내역 2번이상
        - 마지막 시간 23:59 입차되는 경우
        - 주차장에 없는 차량이 출차
        - 주차장에 이미 있는 차량이 다시 입차 
return : 차량번호가 작은 자동차부터 청구할 주차 요금을 차례대로 담은 정수배열 
"""

"""
누적 주차 시간 계산하는 함수 cal_time
Args:
    out_time: 출차 시간
    in_time: 입차 시간
return: 출차 시간 - 입차 시간 (분단위)
"""
def cal_time(in_time, out_time):
    # 출차 시간 out_hour, out_min은 out_time을 :기준으로 나누고 int로 변환
    out_hour, out_min = map(int, out_time.split(':'))
    # 입차 시간 in_hour, in_min은 in_time을 :기준으로 나누고 int로 변환 
    in_hour, in_min = map(int, in_time.split(':'))
    
    # 출차 시간, 입차시간을 분단위로 변환 후 서로 빼서 리턴
    return (out_hour * 60 + out_min) - (in_hour * 60 + in_min)

"""
주차 요금을 계산하는 함수 cal_cost
Args:
    total_time: 누적 주차 시간 
    fees: 요금표 
return: 
    car_cost: 주차요금 
"""
def cal_cost(total_time, fees):
    # 현재 차량의 주차 요금 car_cost는 기본 요금 fees[1]
    car_cost = fees[1]
    # total_time이 기본시간 fees[0]초과하면
    if total_time > fees[0]:
        # 초과한 시간 extra_time 은 total_time - fees[0]
        extra_time = total_time - fees[0] 
        # 초과한 시간에 대해 단위시간으로 나누었을때 몫 extra_time_interval
        extra_time_interval = int(extra_time / fees[2]) + 1 \
                                if extra_time % fees[2] else extra_time // fees[2]
                
        # car_cost에 extra_time_interval만큼 단위요금 fees[3]곱해서 더함 
        car_cost += extra_time_interval * fees[3] 
    
    # car_cost 리턴 
    return car_cost 

def solution(fees, records):
    # 차량번호와 누적 주차 시간을 저장하는 딕셔너리 park_times 생성 
    park_times = dict() 
    # 차량이 입차한 기록을 저장하는 딕셔너리 car_ins 생성. 차량번호:입차시간 
    car_ins = dict()
    # records를 하나씩 탐색하면서 : 원소 record 
    for record in records: 
        # record를 공백 기준으로 time, car_num, is_out으로 나눔 
        time, car_num, is_out = record.split() 
        # is_out이 IN이면
        if is_out == 'IN':
            # car_ins[car_num]에 time 저장 
            car_ins[car_num] = time
            # 반복 진행
            continue
            
        # << is_out이 OUT인 경우 >> 현재 차량의 누적 주차 시간 계산하여 추가 
        # 현재 car_num이 park_times에 있으면 
        if car_num in park_times: 
            # park_times[car_num]에 cal_time호출하여 주차시간을 더함
            park_times[car_num] += cal_time(car_ins[car_num], time)
        # 없으면
        else:
            # park_times[car_num]은 cal_time호출한 주차시간값
            park_times[car_num] = cal_time(car_ins[car_num], time)
        
        # 현재 차량 car_num car_ins에서  입차기록 삭제
        del car_ins[car_num]
            
    # car_ins 키, 값들을 탐색하면서(출차기록이 없는차들 탐색) : 원소 car_num, in_time
    for car_num, in_time in car_ins.items():
        # 23:59분을 출차시간으로 누적 주차 시간 기록 
        # 현재 car_num이 park_times에 있으면
        if car_num in park_times: 
            # park_times[car_num]에 cal_time호출하여 주차시간을 더함
            park_times[car_num] += cal_time(car_ins[car_num], '23:59')
        # 없으면
        else: 
            # park_times[car_num]은 cal_time호출한 주차시간 값
            park_times[car_num] = cal_time(car_ins[car_num], '23:59')
    
    # (차량변호, 누적 요금)을 원소로 하는 리스트 car_costs 빈리스트로 생성
    car_costs = [] 
    # park_times를 items로 하나씩 탐색하면서 : 원소 car_num, park_time
    for car_num, park_times in park_times.items(): 
        # cal_cost로 요금을 계산 후 (car_num, 요금)을 car_costs에 삽입
        car_costs.append((car_num, cal_cost(park_times, fees)))
        
    # car_costs를 정렬하여 요금부분만 리스트로 생성하여 반환
    return [car_cost[1] for car_cost in sorted(car_costs)]