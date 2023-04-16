"""
n * n 정사각형 배열 공백, # 벽으로 이루어짐
지도1중 지도2중 어느 하나라도 벽이면 전체지도에서도 벽
모두 공백인 부분은 전체 지도에서도 공백
둘다 공백이야 공백이고 하나만 벽이면 벽이니 =>  AND 연산을 이용해서 풀이 
지도1, 지도2는 암호화되어있음 => 2진수로 암호화되어있음
십진수를 2진수로 변환하여 각 2진수한자리한자리가 하나의 원소를 가르침 

지도 두개를 원소 하나씩 확인하면서 
10진수 원소를 2진수로 변환하여 and연산하여 최종지도 획득 

"""
def solution(n, arr1, arr2):
    answer = []
    # 인덱스 i - 0부터 n - 1까지 반복하면서 
    for i in range(n):
        total = [] 
        # arr1[i] 을 이진수로 변환 후 문자열로 변환후 인덱스 2부터 슬라이스 하여 0b를 지움 
        map1 = str(bin(arr1[i]))[2:]
        # arr2[i] 을 이진수로 변환 후 문자열로 변환후 인덱스 2부터 슬라이스 하여 0b를 지움 
        map2 = str(bin(arr2[i]))[2:]
                
        # n길이만큼 안되는 문자열은 앞에다 '0'붙여주기 
        while len(map1) < n:
            map1 = '0' + map1
        while len(map2) < n:
            map2 = '0' + map2 
        
        # 이진수로 변환한 두수를 and 연산
        for j in range(len(map2)):
            if map1[j] == '0' and map2[j] == '0':
                total.append(' ')
            else:
                total.append('#')

        # 최종 결과를 answer에 append 
        answer.append(''.join(total))

    return answer