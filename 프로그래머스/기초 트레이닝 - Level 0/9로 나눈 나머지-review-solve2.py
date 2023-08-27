def solution(number):
    return sum([int(num) for num in number.split() if num]) % 9