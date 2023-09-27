import functools

def comparator(a, b):
    num1 = a + b
    num2 = b + a
    
		# num1이 크면 1, num2가 크면 -1, 같으면 0 
    return (int(num1) > int(num2)) - (int(num1) < int(num2))


def solution(numbers):
    str_nums = [str(num) for num in numbers]
    sorted_str_nums = sorted(str_nums, key = functools.cmp_to_key(comparator), reverse = True) 
    
    answer = str(int(''.join(sorted_str_nums)))
    return answer