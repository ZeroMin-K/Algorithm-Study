"""
'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는 길이 5이하의 모든 단어 수록
사전에서 첫번째 단어는 "A". 그다음 "AA". 마지막 단어 "UUUUU"
    - 길이보다 사전순이 먼저 
word: 단어 하나 
return : 이 단어가 사전에서 몇번째 단어인지 
"""


def solution(word):
    # 몇번째 단어인지 값 index 1로 초기화
    index = 1
    # 사전에 있는 단어 dict 'A'로 초기화
    dict = 'A'
    # 알파벳 모음 리스트 alphas 원소 A, E, I, O, U
    alphas = ['A', 'E', 'I', 'O', 'U']
    
    # dict가 word가 다른 동안 반복
    while dict != word: 
        # dict의 길이가 5보다 작으면
        if len(dict) < 5: 
            # dict에 alphas[0] 추가해서 dict 변경
            dict = dict + alphas[0] 
        # dict의 길이가 5이면 
        elif len(dict) == 5: 
            # dict[-1]이 alphas[-1]과 같은 동안
            while dict[-1] == alphas[-1]:
                # dict는 dict의 길이 -1 만큼 슬라이싱
                dict = dict[:len(dict) - 1]
            # 다음 알파벳 next: alphas에서 dict[-1]의 index를 찾아 + 1 했을때 alphas의 인덱스로 한값
            next = alphas[alphas.index(dict[-1]) + 1] 
            # dict는 dict의 길이 - 1만큼 슬라이싱하고 next를 더함 
            dict = dict[:len(dict) - 1] + next 
        # index 1증가 
        index += 1
    
    # 인덱스 리턴 
    return index