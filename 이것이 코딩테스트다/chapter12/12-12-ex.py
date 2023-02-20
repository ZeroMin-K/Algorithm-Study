# 현재 설치된 구조물이 가능한 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 설치된 것이 기둥인 경우
        if stuff == 0:  
            # 바닥 위 혹은 보의 한쪽 끝 부분 위 혹은 다른 기둥위라면 정상
            if y == 0 or [x - 1, y, 1] in answer or \
                [x, y, 1] in answer or \
                [x, y - 1, 0] in answer:
                continue
            # 아니라면 거짓 반환
            return False 
        # 설치된 것이 보인 경우            
        elif stuff == 1: 
            # 한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른 보와 동시에 연결이라면 정상
            if [x, y - 1, 0] in answer or \
                [x + 1, y - 1, 0] in answer or \
                ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                    continue
            # 아니라면 거짓 반환
            return False        
    return True

def solution(n, build_frame):
    answer = []
    # 작업(frame)의 개수는 최대 1000개 
    for frame in build_frame:       
        x, y, stuff, operate = frame

        # 삭제하는 경우 
        if operate == 0:        
            # 일단 삭제해본뒤
            answer.remove([x, y, stuff])    
            
            # 가능한 구조물인지 확인    
            if not possible(answer):        
                # 가능한 구조물이 아니라면 다시 설치 
                answer.append([x, y, stuff])    
        
        # 설치하는 경우
        if operate == 1:        
            # 일단 설치 후 
            answer.append([x, y, stuff])        

            # 가능한 구조물인지 확인
            if not possible(answer):        
                # 가능한 구조물이 아니라면 다시 제거
                answer.remove([x, y, stuff])        

    # 정렬된 결과 반환
    return sorted(answer)       