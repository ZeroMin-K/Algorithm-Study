"""
한자리 숫자가 적힌 종이 조각이 흩어짐
흩어진 종이 조각을 붙여 소수를 몇개 만들 수 있는지 
numberes : 각 종이 조각에 적힌 숫자 문자열
return : 종이조각으로 만들 수 있는 소수 몇개인지

numbers의 숫자문자들을 전부 합쳐보면서 소수가 되는지 판별하며 개수세기 
"""

# 소수인지 확인하는 함수 check_prime 선언: 매개변수 primes, num 
def check_prime(num): 
    if num == 0: return False 
    
    # 인덱스의 대한 숫자가 소수인지 확인하는 리스트 primes : True를 값으로 길이는 num + 1 
    primes = [True] * (num + 1) 
    primes[1] = False 
        
    # 인덱스 i: 2부터 num의 제곱근까지 반복하면서 
    for i in range(2, int(num ** 0.5) + 1): 
        # 배수 k 의 값 2
        k = 2 
        # i * k가 num보다 같거나 작은 동안 반복
        while i * k <= num: 
            # primes[i * k]는 False
            primes[i * k] = False
            # k 1증가
            k += 1
            
    # primes[num] 리턴 
    return primes[num] 

def solution(numbers):
    # numbers의 길이 n
    n = len(numbers) 
    # 만들 수 있는 소수들 집합 primes 빈 집합으로 초기화 
    primes = set() 
    # 방문여부 확인하는 visited False를 값으로 numbers길이만큼의 리스트 선언 
    visited = [False] * n 
    
    #  dfs 함수 선언: 매개변수 result
    def dfs(result): 
        # n, primes_num nonlocal로 선언 
        nonlocal n, primes
        
        # result의 길이가 numbers 길이 n보다 길면 
        if len(result) > n: 
            # return 
            return 
            
        # result를 int로 변경하고나서 소수인지 확인했을 때 소수 이면
        if result and check_prime(int(result)): 
            # primes에 int(result)추가 
            primes.add(int(result))

        # 인덱스 i: 0부터 primes_num 길이 n - 1까지 반복하면서  
        for i in range(n): 
            # i를 방문하지 않았으면
            if not visited[i]: 
                # visited[i] 방문처리 
                visited[i] = True 
                # dfs호출 : 인자 numbers[i] + result
                dfs(numbers[i] + result)
                # dfs호출 : 인자 result +numbers[i]
                dfs(result + numbers[i])
                # visitd[i] False로 변경 
                visited[i] = False 
                
    # dfs 호출 
    dfs("")
    
    # primes의 길이 리턴 
    return len(primes)

numbers = "011"
print(solution(numbers))