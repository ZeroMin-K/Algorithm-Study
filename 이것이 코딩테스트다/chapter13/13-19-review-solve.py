"""
n개 수로 이루어진 수열 a1, a2,..an
수와 수 사이에 끼워넣을 수 있는 n - 1개 연산자 (+, -, *, /)
수와 수 사이에 연산자를 하나씩 넣어서 수식 완성. 수의 순서 변경 불가
식의 계산은 연산자 우선순위 무시하고 앞에서부터 진행 
나눗셈은 정수 나눗셈으로 몫만 취함
음수를 양수로 나눌때 양수로 바꾼뒤 몫을 취하고 몫을 음수로 바꿈 
n개의 수, n- 1개의 연산자 => 식의 결과가 최대인것과 최소인것 구함 


"""

# 수의 개수 n 입력
n = int(input())
# n개의 수열 입력 
data = list(map(int, input().split()))
# 합이 N - 1인  4개의 정수 입력( 각 연산자들의 개수) 
# 인덱스 0: +개수, 인덱스 1: -개수, 인덱스 2: x 개수, 인덱스 3: / 개수 
operators = list(map(int, input().split()))

# 식의 결과 최대값 max_result -1e9로 초기화 
max_result = int(-1e9)
# 식의 결과 최소값 min_result 1e9로 초기화 
min_result = int(1e9)

# 재귀함수 선언 - 매개변수 시작하는 수의 인덱스, 연산자 리스트, 연산자 
def calculate(result, num_index, operators):
    # max_result global로 선언
    global max_result
    # min_result global로 선언 
    global min_result 
    
    # 매개변수 시작하는 수의 인덱스가 n이면 (더이상 계산 진행 안함)
    if num_index == n:
        
        print('<<<<<<<>>>>>>>>>>>>>')
        print('현재까지 계산했을때 값: ', result)
        
        # max_result, min_result 계산
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        # return 
        return 
        
    # 인덱스 i: 0부터 4까지 진행하면서
    for i in range(4):
        print('---------')
        print('현재 연산(+:0, -:1, *:2, /:3): ', i)
        print('현재 연산의 개수: ', operators[i])
        
        # 연산자 리스트[i]가 0보다 크면
        if operators[i] > 0:
            # 연산자 리스트[i] 에서 1제거
            operators[i] -= 1
            
            print('현재 결과값: ', result)
            print('현재 숫자 인덱스: ', num_index) 
            print('현재 숫자 값: ', data[num_index])
            print('다음 연산할 숫자 인덱스: ', num_index + 1)
            
            # 현재 연산자에 대해 연산 진행
            if i == 0:
                result += data[num_index]
            elif i == 1:
                result -= data[num_index]
            elif i == 2:
                result *= data[num_index]
            else:
                result = result // data[num_index]
                
            print('지금까지 계산했을때 수: ', result)
                
            # 재귀진행. 다음 연산에 대한 숫자 인덱스, 현재 연산자 리스트, 연산자 
            calculate(result, num_index + 1, operators)
            
            # 연산자 리스트[i] 1증가 
            operators[i] += 1 

calculate(data[0], 1, operators)

# 식의 결과 최댓값 출력
print(max_result)
# 식의 결과 최솟값 출력 
print(min_result)