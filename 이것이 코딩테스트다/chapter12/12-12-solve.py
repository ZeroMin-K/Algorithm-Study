"""
2차원 벽면 n * n 크기 정사각형 격자 형태에 기둥, 보 구조물 설치 - 기둥과 보는 길이가 1인 선분으로 표현
각 격자 1 * 1 크기. 처음에는 비어있음 
기둥
    - 바닥위에 있거나
    - 보의 한쪽 끝부분 위에 있거나
    - 다른 기둥 위에 있어야함
보
    - 한쪽 끝부분이 기동 위에 있거나
    - 양쪽 끝부분이 다른 보와 동시에 연결 
바닥: 벽면의 맨아래 지면
기둥과 보는 격자선의 교차점에 걸치지 않고 격자 칸의 각 변에 정확히 일치하도록 설치 
기둥과 보를 삭제한 후에도 남은 기둥과 보들또한 위 규칙을 만족해야함. 
작업수행시 만족하지 않으면 작업 무시
n: 벽면 크기
build_frame: 기둥과 보 설치, 삭제 작업 순서 담긴 2차원 배열
    - [x, y, a, b]
        - x, y는 기둥, 보 설치, 삭제할 교차점 좌표. 가로좌표, 세로좌표 
        - a: 설치, 삭제할 구조물 종류. 0은 기둥 1은 보
        - b: 설치, 삭제 여부. 0: 삭제, 1: 설치 
    - 벽면 벗어나게 설치X, 바닥에 보설치X. 겹치거나, 없는 구조물삭제X 
    - 교차점 좌표 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 삭제 
        - 기둥: 설치 좌표 x, y. => 기둥 끝 x + 1, y
        - 보: 설치 좌표 x, y => 보의 끝 x, y + 1 
return : [x, y, a]형식의 2차원 리스트
    - x,y : 기둥, 보 교차점
    - a는 구조물 종류. 0 : 기둥, 1: 보
    - x좌표, y좌표 오름차순, 기둥이 보보다 앞에 
    
build_frame을 탐색하면서 각 작업을 수행했을때 조건을 만족하면 그대로 진행, 만족하지 않으면 무시 
조건은 설치된 각 좌표들을 확인하면서 보 설치조건, 기둥 설치조건을 따짐 
"""
# 구조물들이 올바르게 설치됐는지 확인하는 메서드 check - 매개변수 frames 
def check(frames):
    # frames를 하나씩 탐색하면서 - 원소 frame 
    for frame in frames: 
        # frame[0]은 x, frame[1]은 y - x가 가로축, y가 세로축 
        x, y = frame[0], frame[1]
        # frame[2]가 0이면 (기둥이면) - 설치좌표 frame[0], frame[1]. 기둥 끝 좌표 frame[0] + 1, frame[1]
        if frame[2] == 0:
            # 바닥위에 있는지 => frame[0]이 0이면 
            # 보의 한쪽 끝부분위에 있는지 
            # - 보의 왼쪽 끝 부분위에 있는지 => [frame[0] + 1, frame[1], 1]이 frames안에 있는지 
            # - 보의 오른쪽 끝 부분 위에 있는지 => [frame[0] + 1, frame[1] - 1, 1]이 frames안에 있는지
            # 다른 기둥위에 있는지 => [frame[0] + 1, fram[1], 0]이 frames안에 있는지 
            if y == 0  or \
                [x, y, 1] in frames or \
                [x - 1, y , 1] in frames or \
                [x, y - 1, 0] in frames: 
                # 있으면 continue
                continue 
            # 나머지 경우 
            else: 
                # return False 
                return False 
        # frame[2]가 1이면 (보이면) - 설치좌표 frame[0], frame[1]. 보 끝좌표 frame[0], frame[1] + 1
        else:
            # 한쪽 끝부분이 기둥위에 있는지 => 보의 왼쪽이 기둥위에 있거나 보의 오른쪽이 기둥위에 있거나 
            # - 보의 왼쪽 => frame[0], frame[1]이고 기둥의 끝좌표 => 기둥의 좌표는 frame[0] - 1, frame[1]
            # - 보의 오른쪽 => fram[0], frame[1] + 1이고 기둥의 끝 좌표 => 기둥의 좌표는 frame[0] - 1, frame[1] + 1
            # 따라서 [frame[0] - 1, frame[1], 0]이 frames에 있거나 [frame[0] - 1, frame[1] + 1, 0]이 있는지
            # or 양쪽 끝부분이 다른 보와 동시에 연결되어있는지 
            # - 보의 왼쪽 => frame[0], frame[1] => 다른 보의 오른쪽 좌표 => 다른 보의 왼쪽 좌표 => frame[0], frame[1] - 1
            # - 보의 오른쪽 => frame[0], frame[1] + 1 => 다른 보의 왼쪽 좌표 
            # 따라서 [frame[0], frame[1], 0]과 [frame[0], frame[1] + 1, 0]이 frames에 있는지 
            if [x, y - 1, 0] in frames or \
                [x + 1, y - 1, 0] in frames or \
                ([x - 1, y, 1] in frames and [x + 1, y, 1] in frames): 
                continue # 있으면 continue
            # 나머지의 경우 
            else: 
                # return False
                return False
                
    # 전부 탐색했을때는 결국 문제 없음으로 True 리턴
    return True
    

def solution(n, build_frame):
    # 설치된 구조물을 담는 리스트 
    answer = [] 
    
    # build_frame을 하나씩 탐색하면서 - 원소 frame 
    for frame in build_frame: 
        # 설치, 삭제할 구조물
        work_frame = [frame[0], frame[1], frame[2]]
        
        # frame[3]이 1일때 (구조물을 설치할 때)
        if frame[3] == 1: 
            # 작업할 구조물 work_frame를 answer에 append
            answer.append(work_frame)
            # check가 False일때 
            if not check(answer):
                # answer에서 현재 마지막으로 설치한 원소를 pop
                answer.pop() 
        # frame[3]이 0일때 (구조물을 삭제할 때) 
        else: 
            if work_frame in answer:
                answer.remove(work_frame)
            # check가 False일 때 
            if not check(answer): 
                # answer에 현재 구조물을 다시 설치 append
                answer.append(work_frame)
                
    # answer를 오름차순 정렬해서 리턴 
    return sorted(answer)