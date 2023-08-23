"""
여러 사람이 둥글게 앉아서 숫자를 하나씩 차례대로 말하는 게임의 규칙
1. 숫자를 0부터 시작해서 차례대로 말함. 첫번째사람은 0, 두번째 사람 1, ..열번째 사람은 9
2. 10이상의 숫자부터는 한자리씩 끊어서 말함
    - 열한번째 사람은 10의 첫자리 1, 열두번째 사람은 둘째자리 0 
이진법에서 십육진법까지 모든 진법으로 게임 진행 
n: 진법
t: 미리 구할 숫자의 개수
m: 게임 참가 인원
p: 튜브 순서 
return : 튜브가 말해야하는 숫자 t개를 공백없이 차례대로 나타낸 문자열
    - 10 ~ 15 는 A, F로 출력
    
ex1. 2진법, 숫자 개수 4, 인원 2, 순서1
    - 0 : 0, 1 : 1, 2 : 10, 3 : 11, 4 : 100 ...
    - [0], 1, [1], 0, [1], 1, [1], 0, 0
    => "0111"
    
0부터 시작하면서 n진법에 맞게 숫자를 변환 
각 자리수에 따라 변환된 숫자를 분리 시킨 후 해당 게임동안 말해야할 총 숫자들 리스트에 저장 
m명씩 번갈아가면서 p순서에 따라 각 뽑았을때 t가 되면 문자열로 변환해서 리턴 

순서 : 2명일때 순서가 1이면 인덱스 [0], 1, [2], ... 2으로 나눌때 나머지가 0이면 첫번째
      3명일때 순서가 1이면 인덱스 [0], 1, 2, [3], 4, ..3으로 나눌 때 나머지가 0 => 첫번째
             순서가 2이면 인덱스 0, [1], 2, 3, [4],  3으로 나눌 때 나머지가 1 => 두번째 
             순서가 3이면 인덱스 0, 1, [2], 3, 4, [5] .. 3으로 나눌 때 나머지가 2 => 세번째
    => 인덱스를 m명로 나눌 때 나머지가 p - 1인 경우 자신의 순서
"""
# 숫자를 n진법에 맞게 변환 후 각 자리수마다 잘라서 리스트로 리턴하는 함수 convert 선언 : 매개변수 num, 진법 n
def convert(num , n): 
    # 변환된 수의 자리수들을 저장하는 리스트 converted 빈 리스트로 생성
    converted = [] 
    
    if num == 0:
        converted.append(0)
        
    # num이 0보다 큰 동안 반복진행
    while num > 0: 
        # num을 n으로 나눈 나머지 rest
        rest = num % n
        # rest가 9보다 크면 
        if rest > 9: 
            # rest는 10을 빼서 'A'를 아스키 코드로 변환한 것을 더하여 문자로 변경
            rest = chr(rest - 10 + ord('A'))
        # rest를 converted에 삽입
        converted.append(rest) 
        # num은 num을 n으로 나눈 몫
        num //= n 
    
    # converted을 역순으로 리턴 
    return converted[::-1]

def solution(n, t, m, p):
    # 해당 게임동안 전원이 말해야하는 각 숫자들을 저장하는 리스트 total_nums 빈리스트로 초기화 
    total_nums = [] 
    # 게임 진행하는 숫자 num 0으로 초기화
    num = 0 
    # 튜브가 말해야하는 숫자 리스트 빈리스트로 초기화 
    to_says = [] 
    # 반복 진행
    while True: 
        # num을 n진법에 맞게 변환한 리스트를 total_nums에 더함
        total_nums += convert(num, n)        
        # total_nums를 m명씩 번갈아갔을때 p번째에 해당하는 원소들을 모아 놓은 리스트를 to_says로 초기화
        to_says = [str(total_nums[i]) for i in range(len(total_nums)) if i % m == p - 1]

        print('---')
        print('현재 숫자: ', num, ' 변경: ', convert(num, n))
        print('게임 문자열들: ', total_nums)
        print('말해야할 문자열: ', to_says)
        
        # to_says의 길이가 t이면
        if len(to_says) >= t: 
            to_says = to_says[:t]
            # 반복 종료 
            break 
            
        num += 1
    
    # to_says를 문자열로 변환 후 리턴 
    return ''.join(to_says)

print(solution(2, 4, 2, 1))