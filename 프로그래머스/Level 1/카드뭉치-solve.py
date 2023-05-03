"""
영어 단어가 적힌 카드 뭉치 두개 
원하는 카드 뭉치에서 카드를 순서대로 한장씩 사용
한번 사용한 카드는 다시 사용 불가 
카드를 사용하지 않고 다음 카드로 못넘어감
기존에 주어진 카드 뭉치 단어 순서 못바꿈 

문자열로 이루어진 배열 cars1, cards2
원하는 단어 배열 goal
cards1, cards2로 goal 만들 수 있다면 "YES", "NO" 리턴 

goal를 하나씩 탐색하면서 cards1, cards2에 있는지 확인
cards1, cards2에 대해 새로운 리스트 만들면서 goal 단어들을 리스트에 붙이기
cards1, cards2와 cards1, cards2 리스트의 원소 순서가 같으면  yes 다르면 no 

"""

def solution(cards1, cards2, goal):
    # 완성 여부 
    answer = True
    
    # cards1에 대해 새로운 뭉치 리스트 deck1
    deck1 = [] 
    # cards2에 대해 새로운 뭉치 리스트 deck2 
    deck2 = [] 
    # goal를 하나씩 탐색하면서 - 원소 word
    for word in goal: 
        # word가 cards1에 있으면
        if word in cards1:
            # deck1에 append
            deck1.append(word)
        # 아니면
        else:
            # deck2에 append
            deck2.append(word)
    
    # 인덱스 i를 0부터 deck1 길이 -1 만큼 반복하면서
    for i in range(len(deck1)):
        # deck1[i]과 cards1[i]이 다르면
        if deck1[i] != cards1[i]:
            # answer은 False
            answer = False
        
    # 인덱스 i를 0부터 cards2 길이 - 1 만큼 반복하면서
    for i in range(len(deck2)):
        # deck2[i]와 cards2[i]가 다르면
        if deck2[i] != cards2[i]:
            # answer = False
            answer = False
            
    # answer가 True이면 Yes, 아니면 No 반환
    return "Yes" if answer else "No"