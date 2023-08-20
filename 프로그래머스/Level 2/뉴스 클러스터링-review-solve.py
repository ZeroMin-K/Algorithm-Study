"""
자카드 유사도: 집합간의 유사도 검사
J(A, B) 두 집합 A, B사이의 자카드 유사도 
    : 두 집합의 교집합 크기를 두집합의 합집합 크기로 나눈값으로 정의
    - A, B 모두 공집합일 때 1로 정의 
    - 원소의 중복을 허용하는 다중집합에 대해 확장 가능 
    - 교집합은 중복원소중 작은 개수로, 합집합은 큰 개수로
문자열 사이의 유사도 계산
두글자씩 끊어서 다중 집합 만듬
입력 문자열 str1, str2
두 글자씩 끊어서 다중 집합의 원소 만듬
영문자로된 글자쌍만 유효 
대문자 소문자 차이 무시 
return : 자카도 유사도에 63336을 곱한후 소수점 아래 버리고 정수부만 출력 
"""

def solution(str1, str2):
    # str1을 두글자씩 끊어서 소문자로된 영문자 문자열 리스트로 변경
    str1_sets = [str1[i: i + 2].lower() for i in range(len(str1) - 1) 
                 if str1[i: i + 2].isalpha()]
    # str2을 두글자씩 끊어서 소문자로된 영문자 문자열 리스트로 변경
    str2_sets = [str2[i: i + 2].lower() for i in range(len(str2) - 1) 
                 if str2[i : i + 2].isalpha()]
    
    # str1과 str2가 공집합이면
    if len(str1_sets) == 0 and len(str2_sets) == 0:
        # 65536 리턴 
        return 65536
    
    # 교집합 개수를 저장하는 intersection 0으로 초기화
    intersection = 0
    # 합집합 개수 저장하는 union 0으로 초기화
    union = 0
    
    # str1 + str2를 하나씩 탐색하면서 : 원소 word
    for word in set(str1_sets + str2_sets): 
        # word가 str1과 str2에 있으면
        if word in str1_sets and word in str2_sets:
            # str1에서 word 개수 num1 count를 이용
            num1 = str1_sets.count(word)
            # str2에서 word 개수 num2 count를 이용
            num2 = str2_sets.count(word) 
            # intersection에 num1, num2 중 작은것으로 더함
            intersection += min(num1, num2)
            # union에 num1, num2중 큰 것으로 더함
            union += max(num1, num2)
        # word가 str1에 있으면
        elif word in str1_sets:
            # union에 str1에서 word를 카운트해서 더함
            union += str1_sets.count(word)
        # word가 str2에 잇으면
        elif word in str2_sets:
            # union에 str2에서 word를 카운트해서 더함 
            union += str2_sets.count(word) 
            
    # intersection / union * 65536 곱한 후 정수부만 출력하기 
    return int(intersection / union * 65536)