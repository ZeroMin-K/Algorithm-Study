"""
n미터 벽 - 1미터 길이 구역 n개로 나누어 왼쪽부터 순서대로 1번부터 n번 번호 
벽에 페인트를 칠하는 롤러의 길이 m미터
롤러로 벽에 페인트 한번 칠하는 규칙
    - 롤러가 벽에서 벗어나면 안되고 구역 일부분만 포함되도록 칠하면 안됨 
롤러의 좌우측 끝을 구역의 경계선 혹은 벽의 좌우측 끝부분에 맞춘 후 롤러를 위아래로 움직이면서 벽칠함
현재 페인트를 칠하는 구역들을 완전히 칠한 후 벽에서 롤러 떼며 벽을 한번 칠했다 정의 
한구역에 페인트 여러벌 칠하기 가능. 다시 칠해야할 구역이 아닌곳도 페인트칠 가능
다시 칠하기로 정한 구역은 적어도 한번 페인트 칠하기
롤러로 페인트칠을 하는 횟수 최소화 

n, m. 다시 페인트 칠하기로 정한 구역번호 담긴 배열 section
롤러로 페인트 칠해야하는 최소 횟수 리턴 

최소 횟수는 최대한 롤러끝마다 계속 칠하게하는 것
그리고 마지막 롤러는 마지막 인덱스에 딱맞게 들어가야함 
중복으로 색칠이되도 문제가 없기때문에 최종적으로 색칠하는 곳이 마지막 인덱스 위치 

section하나씩 반복하면서 
    현재 위치가 색칠된 곳이면
        다음 곳으로 
    현재 위치가 색칠된 곳이 아니면
        마지막까지 색칠된 부분을 최신화 
        롤러 색칠 횟수 증가 
        마지막 색칠된부분이 마지막 인덱스보다 크면 종료 
""" 

def solution(n, m, section):
    # 페인트칠 횟수 
    answer = 0
    
    # 페인트칠이 된 마지막 인덱스
    index = -1 
    # section하나씩 반복하면서 - 현재 위치 loc
    for loc in section: 
        # 현재 위치 loc가 인덱스보다 작거나 같으면 (따로 처리를 안하니 로직 불필요 )
            # 다음 부분으로
        # 현재 위치 loc가 마지막 색칠 인덱스보다 크면
        if (loc - 1) >= index:
            # 현재 위치에서 롤러 길이 m만큼 칠함 => 마지막 색칠된 인덱스 최신화
            index = loc - 1 + m             
            # 페인트칠 횟수 answer 1 증가
            answer += 1
            # 마지막 색칠된 인덱스가 n보다 크면
            if index >= n:
                # 종료 
                break
    
    return answer