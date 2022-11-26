array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(result)

array = [('바나나', 2), ('사과', 50), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)
print(result)

array = [('바나나', 2), ('사과', 50), ('당근', 3)]

result = sorted(array, key = lambda x: x[1])
print(result)