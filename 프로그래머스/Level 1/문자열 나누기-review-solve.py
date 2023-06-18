"""
규칙에 따라 문자열 s분해
1. 첫글자 읽음. 첫글자 x
2. 문자열을 왼쪽에서 오른쪽으로 읽으면서 x와 x가 아닌 다른 글자들이 나온 횟수 셈
    - 처음으로 두 횟수가 같아지는 순간 정지. 지금까지 읽은 문자열 분리
3. s에서 분리한 문자열을 빼고 남은 부분에 대해 과정 반복. 남은 부분이 없다면 종료
4. 두 횟수가 다른 상태에서 더이상 읽을 글자 없으면 지금까지 읽은 문자열 분리. 종료.

문자열 분해후 분해한 문자열 개수 리턴 

"""

def solution(s):
    # 분해한 문자열 개수 0으로 초기화 
    answer = 0
    
    # 문자열 s의 길이가 0보다 큰 동안
    while len(s) > 0:
        # x는 문자열의 첫글자
        x = s[0] 
        
        # x가 나오는 횟수 x_count 0으로 초기화
        x_count = 0
        # x가 아닌 횟수 other_count 0으로 초기화
        other_count = 0
        
        # 인덱스 i : 0부터 s의 길이 - 1 까지 반복하면서 
        for i in range(len(s)):
            # s[i]가 x이면 
            if s[i] == x:
                # x_count 1증가
                x_count += 1
            # 나머지 (s[i]가 x가 아니면)
            else: 
                # other_count 1증가 
                other_count += 1
                
            # x_count와 other_count가 같으면
            if x_count == other_count: 
                # i가 s의 길이보다 작으면
                if i < len(s):
                    # 분해한 문자열 개수 answer 1증가
                    answer += 1
                    # s는 i+1부터 슬라이싱
                    s = s[i + 1: ]
                    # 문자열 도는 거 종료 
                    break
        # 문자열 전부 돌았는데 중간에 멈추지 않으면
        else:
            # 문자열 그대로 분리 종료
            answer += 1
            break
                
    return answer