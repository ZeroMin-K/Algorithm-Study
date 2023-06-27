"""
자연수 n을 연속한 자연수들로 표현하기
연속된 자연수들로 n을 표현하는 방법의 수를 리턴 
매번 합을 구하는 것을 비효율적. 누적합을 이용
"""

def solution(n):
    # 표현하는 방법의 수 answer 0으로 초기화 
    answer = 0
    # n + 1 길이의 값은 자신의 인덱스에 값을 갖는 누적합 리스트 prefix_sum 
    prefix_sum = [num for num in range(n + 1)]  
    # 인덱스 i: 1부터 prefix_sum 길이 -1 까지 반복하면서
    for i in range(1, len(prefix_sum)):
        # prefix_sum[i]의 값은 i - 1에서 값을 더한 것 
        prefix_sum[i] += prefix_sum[i - 1] 
        
    # prefix_sum에서 enumerate를 통해 인덱스와 값을 확인하면서 
    # 누적합이 n을 넘어가는 인덱스가 연속할 수 있는 자연수의 최대값
    limit = [i for i, v in enumerate(prefix_sum) if v >= n][0]
        
    # 인덱스 repeat: 1부터 limit까지 반복하면서 - repeat는 몇번 연속되는지
    for repeat in range(1, limit + 1): 
        # 인덱스 start: 1부터 n까지 반복하면서 - start는 연속된 수들중 첫번째 수 (누적합의 시작인덱스)
        for start in range(1, n + 1):
            # 끝인덱스 end는 start + repeat - 1
            end = start + repeat - 1
            # 끝인덱스가 n보다 크면 연속 개수 안 맞으니 반복 넘어감 
            if end > n: 
                break
                
            # 연속된 수의 합 total 은 prefix_sum[end]에서 prefix_sum[start-1]
            total = prefix_sum[end] - prefix_sum[start - 1]
            
            # total이 n과 같으면
            if total == n: 
                # answer 1 증가
                answer += 1
                # 반복 종료
                break 
            # total이 n보다 크면 
            elif total > n: 
                # 반복 종료 
                break 
                
    return answer