import sys
sys.setrecursionlimit(10**6)

"""
문자열 s의 첫글자 x
왼쪽에서 오른쪽으로 읽어나가면서 x와 x가 아닌 다른 글자들이 나온 횟수 각각 셈
처음으로 두 횟수가 같아지는 순간 멈추고 지금까지 읽은 문자열 분리
s에서 분리한 문자열을 빼고 남은부분에 대해 과정 반복
남은 부분 없으면 종료
만약 두 횟수가 다른 상태에서 더이상 읽을 글자 없다면 지금까지 읽은 문자열 분리 종료 
분해한 문자열 개수 리턴 
"""
# 분해 함수 - 분해할 문자열 s
def discompose(s, disassembles): 
    # 분해할 문자열 s가 비어있으면 
    if len(s) == 0: 
        # 리턴 
        return 
    
    # x는 문자열 s의 첫글자
    x = s[0]
    # x의 등장횟수 x_count 0으로 초기화
    x_count = 1
    # x가 아닌 다른 글자 등장 횟수 other_count 0으로 초기화
    other_count = 0
    
    # 인덱스 i : 1부터 문자열 s길이 -1 만큼 반복하면서
    for i in range(1, len(s)):
        # s[i]가 x와 같으면 
        if s[i] == x: 
            # x의 등장횟수 x_count 1증가
            x_count += 1
        # 다르면
        else: 
            # 나머지 등장 횟수 other_count 1 증가
            other_count += 1
    
        # x의 등장횟수, 나머지 등장횟수가 같으면
        if x_count == other_count:
            # 문자열 s를 i-1번째 인덱스까지 슬라이스하고 분해할 문자열 담는 리스트에 append
            disassembles.append(s[:i + 1])
            
            # print("s: ", s)
            # print("x: ", x)
            # print("left: ", s[:i])
            # print('right: ', s[i:])
            # print('dis: ', disassembles)
            
            if i < len(s) - 1: 
                # 문자열 s i번째부터 남은 부분을 다시 분해함수에 넣기 
                discompose(s[i + 1:], disassembles)
                # break
                
            break 
    else: 
        disassembles.append(s)
                

def solution(s):
    # 분해한 문자열을 담는 리스트 disassembles 빈리스트로 초기화 
    disassembles = [] 
    # 분해함수에 문자열 s을 인자로 해서 호출
    discompose(s, disassembles) 
    
    print(disassembles)
    
    # 분해한 문자열담는 리스트 disassembles의 길이 리턴 
    return len(disassembles)