""" 
한변의 길이가 n인 정사각형 배열 의 지도 - 각 칸은 공백 or 벽(#)
두장 지도 겹쳐서 전체 지도 만듬
    한쪽이 벽이면 전체지도도 벽, 둘다 공백이면 전체지도 공백 => OR 연산 
지도1, 지도2는 정수배열로 암호화 
벽1, 공백0 의 한 행은 이진수 숫자 
해독해서 #, 공백으로  구성된 문자열 배열로 출력

"""

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        data = bin(arr1[i] | arr2[i])[2:]
        while len(data) < n:
            data = '0' + data
            
        data = data.replace('0', ' ')
        data = data.replace('1', '#')
        answer.append(data)
        
    return answer