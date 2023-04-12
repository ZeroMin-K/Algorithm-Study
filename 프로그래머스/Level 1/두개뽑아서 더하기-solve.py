"""
리스트에서 서로 다른 인덱스에 있는 두개 수 뽑아 만들 수 있는 모든 수를 리스트에 담아 오름차순으로 정렬 후 리턴

- for문을 두번 사용해서 전부 탐색해서 더한 후 결과 리스트에 없으면 넣어서 최종적으로 오름차순으로 정렬 후 리턴
- combinations를 이용하여 두개의 수를 뽑아서 더한후 결과리스트에 해당값이 없으면 넣어서 최종적으로 오름차순으로 정렬후 리턴 
"""

def solution(numbers):
    answer = []
    # 인덱스 i - 0부터 마지막 인덱스를 제외해서 탐색 진행
    for i in range(len(numbers) - 1):
        # 인덱스 j - i 보다 1큰 상태에서 시작해서 마지막 인덱스 까지 진행 
        for j in range(i + 1, len(numbers)):
            # 인덱스 i에 있는 수와 인덱스j에 있는 수를 더해서 결과리스트에 없으면
            number = numbers[i] + numbers[j]
            if number not in answer:
                # 결과 리스트에 더하기
                answer.append(number)
    # 결과리스트 정렬하기 
    answer.sort()
    return answer