"""
카드 뭉치 두개, 단어들을 사용해 원하는 순서의 단어 배열 만들 수 있는지 
- 원하는 카드 뭉치에서 카드를 순서대로 한장씩 사용
- 한번 사용한 카드 다시 사용 불가
- 카드를 사용하지 않고 다음 카드로 못 넘어감
- 기존에 주어진 카드 뭉치 순서 변경 불가 

두개의 카드 뭉치를 deque로 만들어 goal의 단어들을 하나씩 탐색하면서
가장 앞에 있는 단어가 일치하면 popleft진행하고
둘다 popleft가 안되면 만들 수 없음 

"""
from collections import deque 

def solution(cards1, cards2, goal):
    
    # cards1, cards2를 deque로 변경
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    # goal의 원소들을 하나씩 탐색하면서 - 원소 word
    for word in goal:
        # cards1 길이가 0이 아니고 word와 cards1의 첫번째 원소가 같으면
        if len(cards1) > 0 and word == cards1[0]:
            # cards1 popleft
            cards1.popleft()
        # 혹은 cards2 길이가 0이 아니고 word와 cards2의 첫번째 원소가 같으면
        elif len(cards2) > 0 and word == cards2[0]:
            # cards2 popleft
            cards2.popleft()
        # 둘다 아니면 만들수없는 단어 
        else:
            # No 반환
            return "No"
    
    # 반복을 다 돌았다는 것은 만들 수있는 단어
    return "Yes"