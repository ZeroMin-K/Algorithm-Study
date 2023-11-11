"""
'aya', 'ye', 'woo', 'ma' 네가지 발음을 최대 한번씩 사용해 
이어붙여 조합한 발음밖에 하지 못함
babbing : 문자열 배열
return : 발음할 수 있는 단어 개수
"""

def solution(babblings):
    count = 0
    words = ['aya', 'ye', 'woo', 'ma']
    for babbling in babblings: 
        for word in words:
            if word in babbling:
                babbling = babbling.replace(word, '0')
                
        for ba in babbling:
            if ba != '0': break
        else:
            count += 1
        
    return count