"""
자카드 유사도: 집합간의 유사도를 검사하는 방법 중 하나
    - 두 집합 A, B사이 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두집합의 합집합크기로 나눈 값 
    - 두 집합이 모두 공집합일 경우 1로 정의 
    - 원소의 중복을 허용하는 다중집합에 대해 확장가능
        - 교집합은 원소가 더적은 것으로 
        - 합집합은 원소가 더 많은것으로 
str1, str2: 두 문자열 
문자열은 두 글자씩 끊어서 다중집합의 원소 만듬
영문자로된 글자쌍만 유효. 
    - 기타 공백, 숫자, 특수문자는 버림
대문자와 소문자의 차이 무시 
return : 두 문자열의 자카드 유사도 출력. 65536을 곱한 후 소수점 아래를 버리고 정수부만 출력

문자열의 공백, 숫자, 특수문자는 전부 버리고
비교하기 편하게 전부 소문자로 변경 
문자열을 두 글자씩 집합으로 만든 후 교집합, 합집합을 찾아서 유사도 리턴 
"""
def solution(str1, str2):    
    str1_sets = [''.join(str1[i: i + 2]) for i in range(len(str1) - 1)]
    str2_sets = [''.join(str2[i: i + 2]) for i in range(len(str2) - 1)]
    
    str1_sets = [str1_set.lower() for str1_set in str1_sets 
                                    if str1_set[0].isalpha() and str1_set[1].isalpha()]
    str2_sets = [str2_set.lower() for str2_set in str2_sets 
                                    if str2_set[0].isalpha() and str2_set[1].isalpha()]
    
    if len(str1_sets) == 0 and len(str2_sets) == 0:
        return 65536
    
    str1_sets_dict = dict()    
    str2_sets_dict = dict()
    
    for word in str1_sets:
        if word in str1_sets_dict:
            str1_sets_dict[word] += 1
        else:
            str1_sets_dict[word] = 1
            
    for word in str2_sets:
        if word in str2_sets_dict:
            str2_sets_dict[word] += 1
        else: 
            str2_sets_dict[word] = 1
    
    intersection_key_set = set(str1_sets_dict.keys()) & set(str2_sets_dict.keys())
    union_key_set = set(str1_sets_dict.keys()) | set(str2_sets_dict.keys())
    
    intersection = 0
    union = 0
    for key in intersection_key_set:
        intersection += min(str1_sets_dict[key], str2_sets_dict[key])

    for key in union_key_set:
        if key in str1_sets_dict and key in str2_sets_dict:
            union += max(str1_sets_dict[key], str2_sets_dict[key])
        elif key in str1_sets_dict:
            union += str1_sets_dict[key]
        else:
            union += str2_sets_dict[key]
    
    return int(intersection / union * 65536)