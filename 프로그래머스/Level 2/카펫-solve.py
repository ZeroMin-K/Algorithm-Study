"""
중앙은 노란색, 테두리 1줄은 갈색의 격자모양 카펫
brown: 갈색 격자수
yellow: 노란색 격자수
카페의 가로, 세로 크기 배열 리턴 
카펫의 가로길이는 세로길이와 같거나 세로길이보다 김 => 정사각형 카펫 or 가로가 긴 직사각형 카펫
카펫 총 격자수 = brown + yellow => 격자 가로 * 세로 
최대 총 격자수 => 2,005,000 => 가로를 정사각형에서 늘리고 세로를 정사각형에서 줄이면서 
    가로 * 세로가 총 격자수와 맞으면 정답 
"""

def solution(brown, yellow):
    answer = []
    total = brown + yellow 
    
    for width in range(int(total ** 0.5), total + 1):
        if (total / width) % 1 == 0:
            height = total / width 
            if width >= height and (width - 2) * (height - 2) == yellow:
                answer.append(width)
                answer.append(height) 
                break
    
    return answer